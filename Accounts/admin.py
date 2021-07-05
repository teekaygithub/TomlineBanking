from Accounts.models import Account
from django.contrib import admin

class AccountAdmin(admin.ModelAdmin):
    list_display= ("id", "user", "type", "date_created", "is_active",)

# Register your models here.
admin.site.register(Account, AccountAdmin)