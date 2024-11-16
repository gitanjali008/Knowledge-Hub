from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact  # Import the Contact model

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Correcting the variable name to `name` instead of `username`
        contact = Contact(username=name, email=email, password=password)
        contact.save()
    return render(request, 'contact.html')


def practice(request):
    return HttpResponse("This is a practice page")

def course_outline(request):
    return render(request, 'course_outline.html')

def faculty(request):
    return render(request, 'faculty.html')