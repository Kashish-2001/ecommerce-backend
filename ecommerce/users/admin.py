from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Detail',
            {
                'fields': ('name', 'phone',)
            }
        )
    )

@admin.register(CustomUser)
class CustomAdminUser(admin.ModelAdmin):
    list_display = ("name", "phone","is_staff", "is_superuser")


# admin.site.register(CustomUser, CustomUserAdmin)