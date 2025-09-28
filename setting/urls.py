from django.urls import path
from .views import InfoAPIView

urlpatterns = [
    path("info/", InfoAPIView.as_view(), name="info"),
]