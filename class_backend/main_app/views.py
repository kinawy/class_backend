from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import UserSerializer, TeacherSerializer, StudentSerializer
from .models import User, Teacher, Student
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class TeacherRecordView(APIView):

    # A class based view for creating and fetching teacher records

    def get(self, format=None):

        # Get all the teacher records
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):

        # Create a teacher

        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error.messages, status=status.HTTP_400_BAD_REQUEST)

class StudentRecordView(APIView):

    # A class based view for creating and fetching teacher records

    def get(self, format=None):

        # Get all the teacher records
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):

        # Create a teacher

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error.messages, status=status.HTTP_400_BAD_REQUEST)

class UserRecordView(APIView):

    # A class based view for creating and fetching teacher records

    def get(self, format=None):

        # Get all the teacher records
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):

        # Create a teacher

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error.messages, status=status.HTTP_400_BAD_REQUEST)