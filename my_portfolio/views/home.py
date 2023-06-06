from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import (
    About_me,
    Experience,
    Education,
    Skills,
    Projects,
)
from ..serializer import(
    About_meSerializer,
    ExperienceSerializer,
    EducationSerializer,
    SkillsSerializer,
    ProjectsSerializer,
)

class Home(APIView):
    def get(self, request:Request):
        about_me = About_me.objects.all()
        experience = Experience.objects.all()
        education = Education.objects.all()
        skills = Skills.objects.all()
        about_me_serializer = About_meSerializer(about_me, many=True)
        experience_serializer = ExperienceSerializer(experience, many=True)
        education_serializer = EducationSerializer(education, many=True)
        skills_serializer = SkillsSerializer(skills, many=True)
        
        data = {
            "about_me": about_me_serializer.data,
            "experience": experience_serializer.data,
            "education": education_serializer.data,
            "skills": skills_serializer.data,
        }
        return render(request, "home.html", context=data)