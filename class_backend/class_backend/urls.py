"""class_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from main_app import views

admin.autodiscover()
router = routers.DefaultRouter()
# router.register(r'_', views._View, '_')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    # path('signup/', )
    # path('token-auth/', obtain_jwt_token)
]

urlpatterns += format_suffix_patterns([
    url(r'^api/student/$',
        views.StudentRecordView.as_view(),
        name='student_list'),
    url(r'^api/teacher/$',
        views.TeacherRecordView.as_view(),
        name='teachers_list'),
    url(r'^api/user/(?P<pk>[0-9]+)/',
        views.UserRecordView.as_view(),
        name='user'),
    url(r'^api/users/$',
        views.UsersRecordView.as_view(),
        name='users_list'),
    url(r'^api/classroom/(?P<pk>[0-9]+)/',
        views.ClassroomRecordView.as_view(),
        name='classroom'),
    url(r'^api/classrooms/$',
        views.ClassroomsRecordView.as_view(),
        name='classrooms'),
])
