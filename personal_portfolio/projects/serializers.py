from rest_framework import serializers

from .models import Project, Category, Technology

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'name')


# need to prefetch_related and select_related to avoid (N + 1 problem)
class ProjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    technologies = TechnologySerializer(many=True)
    class Meta:
        model = Project
        fields = ('id', 'overview', 'github', 'image', 'category', 'technologies')