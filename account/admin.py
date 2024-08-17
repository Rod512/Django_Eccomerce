from django.contrib import admin
from .models import Account, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html


class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','is_active')
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    def thubmnail(self, object):
        return format_html('<img src={} width="30" style="border-redius:50%;">'.format(object.profile_picture.url))
    thubmnail.short_description = 'Profile Picture'
    list_display = ('thubmnail', 'user', 'city', 'state', 'country')

admin.site.register(UserProfile, UserProfileAdmin)