from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import Post

UserModel = get_user_model()


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username',)
        read_only_fields  = fields


class PostSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer()
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'creator', 'active', 'date_created', 'date_updated')
