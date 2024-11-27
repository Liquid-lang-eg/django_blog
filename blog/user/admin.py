from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
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
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "age", 'is_superuser', 'is_staff')
    list_filter = ("is_staff", "is_superuser", "is_active",)
    search_fields = ('username',)
