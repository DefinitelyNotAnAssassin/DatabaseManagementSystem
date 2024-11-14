from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from UserAuthentication.models import Account

# Register your models here.


admin.site.register(Account, UserAdmin)
