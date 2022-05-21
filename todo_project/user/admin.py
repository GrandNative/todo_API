from django.contrib import admin
from . import models
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


# ---------------------------------------------------
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = models.TodoUser
    list_display = ['id', "email", "username", ]


admin.site.register(models.TodoUser, CustomUserAdmin)
# ---------------------------------------------------


@admin.register(models.Task)
class VotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_checked', 'title', 'importance', 'note', 'owner')


@admin.register(models.SubTask)
class VotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_checked', 'task_id')
