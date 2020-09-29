from rest_framework import serializers, status

from .models import User, Teacher, Student, GradedAssignments, Classroom, ClassroomsAssignments, StudentsClassrooms, Assignment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_teacher', 'password')

class TeacherSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Teacher
        fields = ('id', 'user')

        def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            teacher, created = Teacher.objects.update_or_create(user=user)

            return teacher

class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = ('id', 'user')

        def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            student, created = Student.objects.update_or_create(user=user)

            return student
