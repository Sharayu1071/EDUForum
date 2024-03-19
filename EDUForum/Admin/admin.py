from django.contrib import admin

# Register your models here.
from .models import UserData
# from .models import UserData_0
@admin.register(UserData)
# @admin.register(UserData_0)

class Userdetails(admin.ModelAdmin):
   list_display = ['username','email','password']

# class Userdetails_0(admin.ModelAdmin):
#    list_display = ['email','password']