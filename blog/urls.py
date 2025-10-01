from django.urls import path
from . import views
urlpatterns = [
    path('', views.BlogListAPIView.as_view(), name='blog-list'),
    path('<slug:slug>/', views.ProjectDetailAPIView.as_view(), name='blog-detail'),
]
