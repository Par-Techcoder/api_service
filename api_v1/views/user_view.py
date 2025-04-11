from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_v1.services.user_service import *
from api_v1.serializers.user_serializer import UserSerializer

class UserListCreateAPIView(APIView):

    def get(self, request):
        users = get_all_user()
        if not users:
            return Response({"message": "No users found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = user_create(serializer.validated_data)
            if not user:
                return Response({"message": "User creation failed."}, status=status.HTTP_400_BAD_REQUEST)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
