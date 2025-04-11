from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from api_v1.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    model = User
    list_display = (
        'id', 'email', 'first_name', 'middle_name', 'last_name',
        'profile_photo_url', 'gender', 'dob', 'address', 'date_joined',
        'is_active', 'is_staff', 'is_superuser'
    )
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'gender')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    # Customize the fieldsets shown in admin for view/edit user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': (
                'first_name', 'middle_name', 'last_name', 'dob', 'gender',
                'profile_photo_url', 'address'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields used when creating a user through admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'first_name', 'middle_name', 'last_name',
                'dob', 'gender', 'profile_photo_url', 'address',
                'is_active', 'is_staff', 'is_superuser',
            ),
        }),
    )
