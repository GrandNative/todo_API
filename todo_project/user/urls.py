from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api', views.UserTasksList.as_view(), name='index'),
    path('user/create', views.CreateUser.as_view(), name='index'),
]
