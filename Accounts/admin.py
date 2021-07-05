from Accounts.models import Account
from django.contrib import admin

class AccountAdmin(admin.ModelAdmin):
    list_display= ("description", "is_active", "user")

# Register your models here.
admin.site.register(Account, AccountAdmin)