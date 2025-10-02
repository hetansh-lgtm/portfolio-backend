from django.urls import path
from .views import APIRoot, ProjectListView, ContactCreateView

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
]
