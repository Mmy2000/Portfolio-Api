# serializers.py
from rest_framework import serializers
from .models import Post , PostCategory , PostImages


class ImageBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ["id", "image"]


class BlogListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "image",
            "cover_description",
            "category",
            "tags",
            "created_at",
        ]


class BlogsDetailsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    images = ImageBlogSerializer(source="post_image", many=True, read_only=True)
    tags = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)

    class Meta:
        model = Post
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
            "images",
        ]
