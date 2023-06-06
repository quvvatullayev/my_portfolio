from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import (
    About_me,
)
from ..serializer import(
    About_meSerializer,
)

class Add_about_me(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = About_meSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class About_me_list(APIView):
    def get(self, request:Request):
        about_me = About_me.objects.all()
        serializer = About_meSerializer(about_me, many=True)
        return Response(serializer.data)