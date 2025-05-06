from django.shortcuts import render
from account.services import AccountServices
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from app.utils import format_exception
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

# Create your views here.
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class RegisterView(APIView):
    # serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        msg = AccountServices.register_user(data)
        return Response(msg, status=HTTP_201_CREATED)
    
    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh", None)
        if not refresh_token:
            return format_exception({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def handle_exception(self, exc):
        return format_exception(exc, self.request)