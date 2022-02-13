from rest_framework.views import APIView
from rest_framework import generics
from .responseObj import ResponseEntity

from .models import Project, Step
from .serializers import ProjectSerializer


class ProjectView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all().order_by('order_num')
        return queryset
