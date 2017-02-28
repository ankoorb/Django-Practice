from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'phone', 'website', 'user_info')

    def user_info(self, obj):
        return obj.description # description row for user

    # Order the users in an order for admin
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user', 'phone') # Reverse order queryset.order_by('-user')
        return queryset

    user_info.short_description = 'Info'





# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
#admin.site.site_header = 'Administration'