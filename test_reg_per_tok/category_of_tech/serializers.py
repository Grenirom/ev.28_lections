from rest_framework import serializers

from category_of_tech.models import Category, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class ListCategorySerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'
