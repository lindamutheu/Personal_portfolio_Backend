from django.shortcuts import render
from rest_framework import generics
from .models import Profile, Project, Experience, Education, ContactMessage
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    ExperienceSerializer,
    EducationSerializer,
    ContactMessageSerializer
)

class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.first()


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer

class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all().order_by("-start_date")
    serializer_class = ExperienceSerializer


class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all().order_by("-end_year")
    serializer_class = EducationSerializer


class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer





