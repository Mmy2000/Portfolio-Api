from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("about/", include("about.urls")),
    path("setting/", include("setting.urls")),
    path("contact/", include("contact.urls")),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
