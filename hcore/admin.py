from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Account, Member


class AccountAdmin(admin.ModelAdmin):
    fields = ('name',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'account_id', 'account')


admin.site.site_header = 'Mini mPulse'
admin.site.unregister(Group)
admin.site.register(Account, AccountAdmin)
admin.site.register(Member, MemberAdmin)
