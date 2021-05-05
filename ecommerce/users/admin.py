from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    list_display = ("username", "phone", "is_staff", "is_superuser")

    fieldsets = (
        (
            'User Detail',
            {
                'fields': ('name', 'phone',)
            }
        ),
        *UserAdmin.fieldsets

    )

    # fieldsets = (
    #     (None, {'fields': ('name', 'phone',)}),
    # )

# @admin.register(CustomUser)
# class CustomAdminUser):


admin.site.register(CustomUser, CustomUserAdmin,)