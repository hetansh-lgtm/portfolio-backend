from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from .models import Project
from .serializers import ProjectSerializer, ContactSubmissionSerializer

class APIRoot(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response({
            "projects": request.build_absolute_uri(reverse("projects-list")),
            "contact": request.build_absolute_uri(reverse("contact-create")),
        })

class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Project.objects.prefetch_related('technologies').all()

class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSubmissionSerializer
    permission_classes = [permissions.AllowAny]
