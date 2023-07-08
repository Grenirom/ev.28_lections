from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        # fields = ('user_id', 'username')
        fields = '__all__'


class LikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
