from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import UserSerializer, UsersSerializer, TeacherSerializer, StudentSerializer, ClassroomSerializer
from .models import User, Teacher, Student, Classroom
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

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
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class StudentRecordView(APIView):

    # A class based view for creating and fetching student records

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
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class UserRecordView(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        if not user:
            return JsonResponse({'status': 0, 'message': 'User with this id not found'})
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format=None):
        try:
            user = self.get_object(pk)
        except:
            return JsonResponse({'status': 0, 'message': 'User with this id not found'})

        email = request.data.get("email", None)
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.set_password(password)

        try:
            user.save()
            return JsonResponse({'status': 1, 'message': 'Your profile updated successfully!'})
        except:
            return JsonResponse({'status': 0, 'message': 'There was something wrong while updating your profile.'})

    

class UsersRecordView(APIView):

    # A class based view for creating and fetching teacher records

    def get(self, format=None):
        # Get all the teacher records
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        # Create a teacher
        serializer = UserSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid(raise_exception=ValueError):
            # print(serializer)
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class ClassroomRecordView(APIView):

    def get(self, format=None):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)