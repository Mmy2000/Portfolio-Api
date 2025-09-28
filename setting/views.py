from rest_framework import generics
from .models import Info
from .serializers import InfoSerializer
from config.response import CustomResponse


class InfoAPIView(generics.RetrieveAPIView):
    serializer_class = InfoSerializer

    def get_object(self):
        return Info.objects.last()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return CustomResponse(data=serializer.data, status=200)