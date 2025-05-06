from category.views import CategoryBasicView, CategoryDetailView
from django.urls import path

urlpatterns = [
    path('category/', CategoryBasicView.as_view(), name='categories'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category_detail'),
]
