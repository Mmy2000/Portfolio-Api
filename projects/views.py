# views.py
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Projects
from .serializers import ProjectListSerializer, ProjectsDetailsSerializer
from .filters import ProjectFilter
from config.pagination import CustomPagination
from config.response import CustomResponse


class ProjectListAPIView(generics.ListAPIView):
    queryset = (
        Projects.objects.all()
        .select_related("categoryproject", "auther")
        .prefetch_related("tags", "project_image")
    )
    serializer_class = ProjectListSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProjectFilter
    ordering_fields = ["created_at", "title"]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        pagination = None
        if hasattr(self, "paginator") and self.paginator:
            pagination = self.paginator.get_pagination_meta()
            
        response.data["filters"] = ProjectFilter.get_available_filters()
        results = response.data.get("results", response.data)
        return CustomResponse(
            data=results,
            filters=response.data.get("filters", {}),
            status=response.status_code,
            pagination=pagination,
        )


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = (
        Projects.objects.all()
        .select_related("categoryproject", "auther")
        .prefetch_related("tags", "project_image")
    )
    serializer_class = ProjectsDetailsSerializer
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return CustomResponse(data=response.data, status=response.status_code)
