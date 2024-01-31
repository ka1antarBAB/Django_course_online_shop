from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from forms import CustomUserChangeForm, CustomUserCreationForm
from models import CustomUser

user_model = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = user_model
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'email', '')

