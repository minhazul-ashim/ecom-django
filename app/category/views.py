from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.utils import format_exception, format_response
from app.permissions import IsAdminForUnsafeMethods
from category.serializers import CategorySerializer;
from category.models import Category
from app.utils import createUniqueMediaName

class CategoryBasicView(APIView):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = CategorySerializer;

    def get(self, request):
        categories = Category.objects.all();
        serialized_data = self.serializer_class(categories, many=True).data;
        return Response({'message': 'Request Successful', 'data': serialized_data})

    def post(self, request):
        name = request.data['name']
        thumb = request.data['thumb']
        # This utility function generates a unique name for the thumb 
        thumbWithUniqueName = createUniqueMediaName(thumb)
        category = Category.objects.create(name=name, thumb=thumbWithUniqueName)
        serialized_data = self.serializer_class(category).data
        return Response({'message': 'Category Created!', 'data': serialized_data})

    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    


class CategoryDetailView(APIView):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = CategorySerializer
    
    def get(self, request, id):
        targetCategory = Category.objects.filter(id=id).first()
        if not targetCategory:
            return format_response(data='Category not found', status_code=404)
        serialized_data = self.serializer_class(targetCategory).data
        return format_response(data=serialized_data, status_code=200)
    
    def delete(self, request, id):
        target =  Category.objects.filter(id=id).first();
        if not target:
            return format_response(data='Category not found', status_code=404)
        target.delete()
        return format_response(data='Category deleted successfully', status_code=200)
    
    def patch(self, request, id):
        try:
            targetCategory = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return format_response(data='Category not found', status_code=404)

        if 'name' in request.data:
            targetCategory.name = request.data['name']

        if 'thumb' in request.FILES:
            thumb = request.FILES['thumb']
            uniquely_name_file = createUniqueMediaName(thumb)
            targetCategory.thumb = uniquely_name_file

        targetCategory.save()
        serialized_data = self.serializer_class(targetCategory).data
        return format_response(data=serialized_data, status_code=200)

    def handle_exception(self, exc):
        return format_exception(exc, self.request)