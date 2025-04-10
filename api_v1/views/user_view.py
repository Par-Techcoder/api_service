from django.views import View
from django.shortcuts import render


class UserListApi(View):
    def get(self, request):
        return