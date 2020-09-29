from rest_framework import serializers, status
from django.contrib.auth.hashers import make_password
from .models import User, Teacher, Student, GradedAssignments, Classroom, ClassroomsAssignments, StudentsClassrooms, Assignment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_teacher', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        if instance.is_teacher == True:
            Teacher.objects.create(user=instance)
        else:
            Student.objects.create(user=instance)
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class TeacherSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Teacher
        fields = ('id', 'user')

        # def create(self, validated_data):
        #     user_data = validated_data.pop('user')
        #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        #     teacher, created = Teacher.objects.update_or_create(user=user)

        #     return teacher

class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = ('id', 'user')

        # def create(self, validated_data):
        #     user_data = validated_data.pop('user')
        #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        #     student, created = Student.objects.update_or_create(user=user)

        #     return student


