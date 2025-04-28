from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'id_number', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Work Scholar Info', {'fields': ('user_type', 'id_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Work Scholar Info', {'fields': ('user_type', 'id_number')}),
    )
    search_fields = ('username', 'email', 'id_number')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
