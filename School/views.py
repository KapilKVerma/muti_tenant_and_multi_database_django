from django.shortcuts import render

from .models import Student

def get_Students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'templates/index.html', context)