from django.contrib import admin

from .models import *

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['get_user_name','get_full_name','email','address']
    
    def get_user_name(self,obj):
        return obj.user.username
    def get_full_name(self,obj):
        return obj.full_name
    
    get_user_name.short_description = 'User Name'
    get_full_name.short_description = 'User Name'
    
    