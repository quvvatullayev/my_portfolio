from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import (
    Projects,
    About_me,
)
from ..serializer import(
    ProjectsSerializer,
    About_meSerializer,
)


class Add_projects(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = ProjectsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class Projects_list(APIView):
    def get(self, request:Request):
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        data = {
            "projects": serializer.data,
        }
        return render(request, "projects.html", context=data)