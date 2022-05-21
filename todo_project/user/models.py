from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TodoUser(AbstractUser):
    username = models.CharField(max_length=250, null=False, blank=False, unique=True)
    password = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    is_checked = models.BooleanField(default=False, null=False, blank=False)
    title = models.CharField(max_length=250, default='title', null=False, blank=False)
    importance = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline_at = models.DateTimeField(null=True, blank=True)
    note = models.TextField(max_length=250, null=False, blank=False)
    owner = models.ForeignKey(TodoUser, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        data = f'{self.owner.username}: {self.title}'
        return data


class SubTask(models.Model):
    title = models.CharField(max_length=250, default='title', null=False, blank=False)
    is_checked = models.BooleanField(default=False, null=False, blank=False)
    task = models.ForeignKey(Task, blank=False, null=False, on_delete=models.CASCADE)
