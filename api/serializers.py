from rest_framework import serializers
from .models import Technology, Project, ContactSubmission

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", "name", "icon"]

class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "image", "live_link", "github_link", "technologies"]

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ["id", "name", "email", "message", "timestamp"]
        read_only_fields = ["timestamp"]