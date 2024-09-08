from .serializers import UserLoginSerializer
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import generics, status
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

User = get_user_model()


# Register a new user
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                # check if user exists
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'User not found!'}, status=status.HTTP_400_BAD_REQUEST)

            # check if user is active
            if not user.is_active:
                return Response({'error': 'Please activate your account before login!'}, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(request, username=username, password=password)

            # check if username and password are correct
            if user is None:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

            # login user
            login(request, user)

            # creating a token for user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Login successful",
                "token": token.key,
                "user_id": user.id,
                "username": user.username
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        # logout user
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
