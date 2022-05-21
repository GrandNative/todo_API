from rest_framework import serializers
from django.db.models import Q
from django.db.models import F
from . import models
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    sub_tasks = serializers.SerializerMethodField()

    @staticmethod
    def get_sub_tasks(obj):
        sub_tasks = models.SubTask.objects.filter(task=obj)
        return SubTaskSerializer(sub_tasks, many=True).data

    @staticmethod
    def get_owner(obj):
        user = models.TodoUser.objects.get(id=obj.owner.id)
        return UserInfoSerializer(user).data

    class Meta:
        model = models.Task
        fields = (
            'is_checked',
            'title',
            'importance',
            'created_at',
            'updated_at',
            'deadline_at',
            'note',
            'owner',
            'sub_tasks',
        )


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoUser
        fields = (
            'id',
            'username',
            'email',
        )

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "username", "password", )
