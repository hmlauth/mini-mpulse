from django.urls import path
from .views import AccountViewSet, MemberViewSet

urlpatterns = [
    url('members/$', MemberViewSet, name='member-list'),
    url('members/{pk}/$', MemberViewSet, name='member-detail'),
    url('accounts/$', AccountViewSet, name='account-list'),
    url('accounts/{pk}/$', AccountViewSet, name='account-detail')
]