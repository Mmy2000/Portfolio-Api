from django.urls import path
from .views import *

urlpatterns = [
    path('about_me/', AboutRetrieveAPIView.as_view(), name='about_me'),
    path('education/', EducationRetriveAPIView.as_view(), name='education'),
    path('summary/', SummaryRetrieveAPIView.as_view(), name='summary'),
    path('professional_experience/', ProfessionalExperienceListAPIView.as_view(), name='professional_experience'),
]
