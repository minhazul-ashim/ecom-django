from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.utils import format_exception
from app.permissions import IsAdminForUnsafeMethods

class CategoryBasicView(APIView):
    permission_classes = [IsAdminForUnsafeMethods]
    def get(self, request):
        return Response({'message': 'Hello from CategoryBasicView! Get method!'})

    def post(self, request):
        return Response({'message': 'Hello from CategoryBasicView! POST method!'})

    def patch(self, request):
        return Response({'message': 'Hello from CategoryBasicView! Patch method!'})

    def delete(self, request):
        return Response({'message': 'Hello from CategoryBasicView! Delete method!'})

    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    


class CategoryDetailView(APIView):
    def get(self, request, id):
        return Response({'message': f'Detail view for category ID {id}'})