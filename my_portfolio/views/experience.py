from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import (
    Experience,
)
from ..serializer import(
    ExperienceSerializer,
)

class Add_experience(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = ExperienceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class Experience_list(APIView):
    def get(self, request:Request):
        experience = Experience.objects.all()
        serializer = ExperienceSerializer(experience, many=True)
        data = {
            'experiences': serializer.data
        }
        return render(request, 'experience.html', data)
    