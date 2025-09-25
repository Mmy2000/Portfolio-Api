from .models import *
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'


class EXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EXP
        fields = ["id", "subject"]


class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    exp = EXPSerializer(many=True, read_only=True)
    class Meta:
        model = ProfessionalExperience
        fields = '__all__'


class MySkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySkills
        fields = ["id", "name", "percent"]


class CategorySkillsSerializer(serializers.ModelSerializer):
    skills = MySkillsSerializer(source="skills_category", many=True, read_only=True)

    class Meta:
        model = CategorySkills
        fields = ["id", "name", "icon", "skills"]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
