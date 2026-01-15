from .models import Profile, Project, Experience, Education, ContactMessage
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'bio',
            'email',
            'title',
            'location',
            'github_url',
            'linkedin_url',
            'resume',
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'problem_statement',
            'solution',
            'tech_stack',
            'github_url',
            'created_at',
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'job_title',
            'company_name',
            'start_date',
            'end_date',
            'responsibilities',
        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'institution_name',
            'degree',
            'field_of_study',
            'start_year',
            'end_year',
        ]

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'subject',
            'message',
            'sent_at',
        ]

    
