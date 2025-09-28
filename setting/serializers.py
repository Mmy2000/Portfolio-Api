from rest_framework import serializers
from .models import Info, Roles

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id', 'name']

class InfoSerializer(serializers.ModelSerializer):
    role = RolesSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = [
            'id', 'site_name', 'f_name', 'l_name', 'description', 'email', 
            'image', 'role', 'fb_link', 'twitter_link', 
            'instagram_link', 'githup_link', 'linkedin_link'
        ]