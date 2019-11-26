from django.shortcuts import render, redirect
from .models import Course
from . import course_data_scrapper

def course_list(request):
    course_list = course_data_scrapper.get_courses()
    return render(request, 'course/course_list.html', {'course_list': course_list})
