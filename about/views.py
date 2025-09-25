from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from config.pagination import CustomPagination
from config.response import CustomResponse


class AboutRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.last()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return CustomResponse(
            data=serializer.data,
            status=200,
        )

class EducationRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = EducationSerializer

    def get_object(self):
        return Education.objects.last()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return CustomResponse(
            data=serializer.data,
            status=200,
        )

class SummaryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SummarySerializer

    def get_object(self):
        return Summary.objects.last()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return CustomResponse(
            data=serializer.data,
            status=200,
        )

class ProfessionalExperienceListAPIView(generics.ListAPIView):
    queryset = ProfessionalExperience.objects.all().order_by('-year')
    serializer_class = ProfessionalExperienceSerializer
    pagination_class = CustomPagination
    ordering_fields = ["year", "title"]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        pagination = None
        if hasattr(self, "paginator") and self.paginator:
            pagination = self.paginator.get_pagination_meta()
        results = response.data.get("results", response.data)
        return CustomResponse(
            data=results,
            status=response.status_code,
            pagination=pagination,
        )


class CategorySkillsListAPIView(generics.ListAPIView):
    queryset = CategorySkills.objects.prefetch_related("skills_category").all()
    serializer_class = CategorySkillsSerializer
    pagination_class = None  # you can enable if needed

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        results = response.data
        return CustomResponse(
            data=results,
            status=response.status_code,
        )
