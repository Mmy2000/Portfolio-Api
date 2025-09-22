# filters.py
import django_filters
from .models import Projects
from django.db import models
from django.db.models import Min, Max
from django.db.models import Count, Min, Max


class ProjectFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name="categoryproject__name", lookup_expr="iexact"
    )
    tags = django_filters.CharFilter(field_name="tags__name", lookup_expr="iexact")
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr="lte")
    search = django_filters.CharFilter(method="filter_search")

    class Meta:
        model = Projects
        fields = ["category", "tags", "start_date", "end_date", "search"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            models.Q(title__icontains=value) | models.Q(description__icontains=value)
        )

    @staticmethod
    def get_available_filters():
        # Categories with counts
        categories = (
            Projects.objects.values("categoryproject__name")
            .annotate(count=Count("id"))
            .order_by("categoryproject__name")
        )

        # Tags with counts
        tags = (
            Projects.objects.values("tags__name")
            .annotate(count=Count("id"))
            .order_by("tags__name")
        )

        # Date range
        date_range = Projects.objects.aggregate(
            start=Min("created_at"), end=Max("created_at")
        )

        return {
            "category": [
                {"name": c["categoryproject__name"], "count": c["count"]}
                for c in categories
                if c["categoryproject__name"]
            ],
            "tag": [
                {"name": t["tags__name"], "count": t["count"]}
                for t in tags
                if t["tags__name"]
            ],
            "min_date": 
                date_range["start"].date().isoformat() if date_range["start"] else None
            ,
            "max_date": 
                date_range["start"].date().isoformat() if date_range["start"] else None
            
        }
