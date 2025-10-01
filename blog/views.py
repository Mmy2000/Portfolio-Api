from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import BlogListSerializer, BlogsDetailsSerializer
from .filters import BlogFilter
from config.pagination import CustomPagination
from config.response import CustomResponse


class BlogListAPIView(generics.ListAPIView):
    queryset = (
        Post.objects.all()
        .select_related("category", "auther")
        .prefetch_related("tags", "post_image")
    )
    serializer_class = BlogListSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BlogFilter
    ordering_fields = ["created_at", "title"]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        pagination = None
        if hasattr(self, "paginator") and self.paginator:
            pagination = self.paginator.get_pagination_meta()

        response.data["filters"] = BlogFilter.get_available_filters()
        results = response.data.get("results", response.data)
        return CustomResponse(
            data=results,
            filters=response.data.get("filters", {}),
            status=response.status_code,
            pagination=pagination,
        )


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = (
        Post.objects.all()
        .select_related("category", "auther")
        .prefetch_related("tags", "post_image")
    )
    serializer_class = BlogsDetailsSerializer
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return CustomResponse(data=response.data, status=response.status_code)
