from rest_framework import generics, permissions

from category_of_tech.models import Category
from category_of_tech.serializers import ListCategorySerializer


class ListOfCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(), )
        return (permissions.IsAdminUser(), )


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer
    permissions = [permissions.IsAdminUser(), ]

    def get_permissions(self):
        return self.permissions


class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer
    permissions = [permissions.IsAdminUser(), ]

    def get_permissions(self):
        return self.permissions

