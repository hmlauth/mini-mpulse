from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from .models import Account, Member
from .serializers import AccountSerializer, MemberSerializer


BAD_REQUEST_BODY = "Bad request body."
DUPLICATE_PHONE_NUMBER = "Phone number already exists for this account."
DOES_NOT_EXIST = "Member or account does not exist."


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('name')
    serializer_class = AccountSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filterset_fields = ('phone_number', 'client_member_id')

    @action(methods=['GET'], detail=True, url_path='account/(?P<account_id>\d+)', url_name='member-by-given-account')
    def get_member_by_given_account(self, request, account_id, pk=None):
        if pk is not None and account_id is not None:
            try:
                queryset = Member.objects.get(pk=pk, account_id=account_id)
                member = self.serializer_class(queryset)
                return Response(member.data, status.HTTP_200_OK)
            except ObjectDoesNotExist as e:
                print("Exception Occurred: ", e)
                return Response({"response": DOES_NOT_EXIST}, status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=False, url_path='create', url_name='create-bulk-member')
    def create_members(self, request):
        data = request.data.get('members', False)
        if not data or (data and not isinstance(data, list)):
            return Response({"response": BAD_REQUEST_BODY}, status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer = MemberSerializer(data=data, many=True)
            try:
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                print("Exception Occurred: ", e)
                return Response({"response": DUPLICATE_PHONE_NUMBER}, status=status.HTTP_400_BAD_REQUEST)
            except AttributeError as e:
                print("Exception Occurred: ", e)
                return Response(
                    {"response": f"{BAD_REQUEST_BODY} Check that 'account' attribute exists for each record."},
                    status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
