from django.urls import path
from .views import (
    ProfileView,
    ProjectListView,
    ExperienceListView,
    EducationListView,
    ContactMessageCreateView,
)

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('experience/', ExperienceListView.as_view()),
    path('education/', EducationListView.as_view()),
    path('contact/', ContactMessageCreateView.as_view()),
]
    