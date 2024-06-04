from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserChangeForm
from .models import User
from django.contrib.auth.models import Group


# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    # The fields to be used in displaying the User model.
    list_display = ("email", "phone_number" , "is_admin")
    list_filter = ["is_admin"]

    fieldsets = [
        (None, {"fields": ["email", "phone_number","full_name","password"]}),
        ("Permissions", {"fields": ["is_active","is_admin","last_login"]}),
    ]

    add_fieldsets = [
        (None,{"fields":["phone_number","email","full_name","password1","password2"]}),
    ]

    search_fields = ("email","full_name")

    ordering = ("full_name",)

    filter_horizontal = ()
# unregister the Group model from admin.
admin.site.unregister(Group)
# Now register the new UserAdmin...
admin.site.register(User,UserAdmin)