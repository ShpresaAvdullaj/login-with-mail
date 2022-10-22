from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserChangeForm
from .forms import UserCreationForm


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
    list_display = ("email", "first_name", "last_name", "is_staff")
    fieldsets = (
        ("Credentials", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)