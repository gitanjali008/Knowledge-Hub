from django.shortcuts import render, HttpResponse, redirect
from .models import Contact  # Import the Contact model

# Create your views here.
def index(request):
    return render(request, '../index.html')

def about(request):
    return render(request, '../about.html')

def contact(request):
   return render(request, '../contact.html')

def practice(request):
    return HttpResponse("This is a practice page")

def course_outline(request):
    return render(request, '../course_outline.html')

def faculty(request):
    return render(request, '../faculty.html')