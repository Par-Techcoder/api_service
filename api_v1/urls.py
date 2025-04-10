from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListApi.as_view(), name='user-api'),
]
