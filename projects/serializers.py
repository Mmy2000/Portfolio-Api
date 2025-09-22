# serializers.py
from rest_framework import serializers
from .models import Projects, CategoryProject, ImageProject


class ImageProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProject
        fields = ["id", "image"]


class ProjectListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source="categoryproject")
    tags = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "slug",
            "image",
            "cover_description",
            "category",
            "tags",
            "url",
            "created_at",
            "updated_at",
        ]

class ProjectsDetailsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source="categoryproject")
    images = ImageProjectSerializer(source="project_image", many=True, read_only=True)
    tags = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "slug",
            "auther",
            "image",
            "cover_description",
            "description",
            "category",
            "tags",
            "url",
            "client",
            "images",
            "created_at",
        ]
