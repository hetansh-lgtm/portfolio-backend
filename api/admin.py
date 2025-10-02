from django.contrib import admin
from .models import Technology, Project, ContactSubmission

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "icon")
    search_fields = ("name",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "github_link", "live_link", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at",)
    filter_horizontal = ("technologies",)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "timestamp")
    search_fields = ("name", "email", "message")
    readonly_fields = ("timestamp",)