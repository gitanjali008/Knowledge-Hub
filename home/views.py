from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact  # Import the Contact model
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
import json




# Create your views here.
def index(request):
    return render(request, '../templates/index.html')

def about(request):
    return render(request, '../templates/about.html')

def book(request):
    return render(request, '../templates/book.html')
def courses(request):
    return render(request, '../templates/notes-courses.html')

def assignment(request):
    return render(request, '../templates/assignment.html')

def contact(request):
    if request.method == 'POST':
        # Get the fields from the POST data using .get() to avoid errors if a field is missing
        username = request.POST.get('username')
        course = request.POST.get('course')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if all required fields are present
        if not username or not course or not email or not password:
            error_message = "Enter the correct password or username."
            return render(request, 'login.html', {'error_message': error_message})
        
        # Check if the username already exists in the database
        if Contact.objects.filter(username=username).exists():
            error_message = "This username already exists. Please try another."
            return render(request, 'login.html', {'error_message': error_message})

        # Hash the password before saving it
        hashed_password = make_password(password)
        
        # Save the contact in the Contact model
        contact = Contact.objects.create(username=username, course=course, email=email, password=hashed_password)
        contact.save()

        # Redirect to the login page after successful registration
        return redirect('login')

    return render(request, 'login.html')



def pyq(request):
    return render(request, '../templates/pyqs.html')   

def course_outline(request):
    return render(request, '../templates/course_outline.html')

def faculty(request):
    return render(request, '../faculty.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Find the contact by username
        try:
            contact = Contact.objects.get(username=username)
        except Contact.DoesNotExist:
            contact = None
        
        if contact and check_password(password, contact.password):  # Check the hashed password
            # User is authenticated successfully
            return redirect('index')  # Redirect to index page after successful login
        else:
            # If authentication failed
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')


#assignments
def btech(request):
    return render(request, '../templates/btech.html')
def bba(request):
    return render(request, '../templates/bba.html')
def mba(request):
    return render(request, '../templates/mba.html')
def bsc(request):
    return render(request, '../templates/bsc.html')
def mca(request):
    return render(request, '../templates/mca.html')
def mcom(request):
    return render(request, '../templates/mcom.html')
def bcom(request):
    return render(request, '../templates/bcom.html')
def bca(request):
    return render(request, '../templates/bca.html')
def btech_assignment(request):
    return render(request, '../templates/btech_assignment.html')    

def bba_assignment(request):
    return render(request, '../templates/bba_assignment.html')    

def bca_assignment(request):
    return render(request, '../templates/bca_assignment.html')    

def bcom_assignment(request):
    return render(request, '../templates/bcom_assignment.html')    
def mcom_assignment(request):
    return render(request, '../templates/mcom_assignment.html')    
                   



#previous year question paper 

def sem1mathpyqs(request):
    return render(request, '../templates/sem1-math-pyq.html')

def sem1physicspyqs(request):
    return render(request, '../templates/sem1-physics-pyq.html')

def sem1ecepyqs(request):
    return render(request, '../templates/sem1-ece-pyq.html')

def sem2mathpyqs(request):
    return render(request, '../templates/sem2-math-pyq.html')  

def sem2chemistrypyqs(request):
    return render(request, '../templates/sem2-chemistry-pyq.html') 

def sem2evspyqs(request):
    return render(request, '../templates/sem2-evs-pyq.html') 

def sem3OOPSpyqs(request):
    return render(request, '../templates/sem3-OOPS-pyq.html') 

def sem3dspyqs(request):
    return render(request, '../templates/sem3-ds-pyq.html') 

def sem3digitallogicpyqs(request):
    return render(request, '../templates/sem3-digital-logic-pyq.html')

def sem4javapyqs(request):
    return render(request, '../templates/sem4-java-pyq.html')  

def sem4micropyqs(request):
    return render(request, '../templates/sem4-micro-pyq.html')

def sem4Automatapyqs(request):
    return render(request, '../templates/sem4-Automata-pyq.html') 

def sem5mlpyqs(request):
    return render(request, '../templates/sem5-ml-pyq.html')  

def sem5databasepyqs(request):
    return render(request, '../templates/sem5-database-pyq.html') 

def sem5ospyqs(request):
    return render(request, '../templates/sem5-os-pyq.html')  

def sem6compilerpyqs(request):
    return render(request, '../templates/sem6-compiler-pyq.html') 

def sem6sepyqs(request):
    return render(request, '../templates/sem6-se-pyq.html')  

def sem6networksecuritypyqs(request):
    return render(request, '../templates/sem6-network-security-pyq.html') 

def sem7Softpyqs(request):
    return render(request, '../templates/sem7-s oft-pyq.html')   

def sem7bipyqs(request):
    return render(request, '../templates/sem7-bi-pyq.html') 

def sem7cgpyqs(request):
    return render(request, '../templates/sem7-cg-pyq.html') 

def sem8ccpyqs(request):
    return render(request, '../templates/sem8-cc-pyq.html') 

def sem8mbpyqs(request):
    return render(request, '../templates/sem8-mb-pyq.html') 

def sem8dmpyqs(request):
    return render(request, '../templates/sem8-dm-pyq.html') 

def sem1physicspyqs(request):
    return render(request, '../templates/sem1-physics-pyq.html') 

def sem1chemistrypyqs(request):
    return render(request, '../templates/sem1-chemistry-pyq.html')

def sem1mathpyqs(request):
    return render(request, '../templates/sem1-math-pyq.html')  

def sem1englishpyqs(request):
    return render(request, '../templates/sem1-english-pyq.html') 

def sem2physicspyqs(request):
    return render(request, '../templates/sem2-physics-pyq.html') 

def sem2chemistrypyqs(request):
    return render(request, '../templates/sem2-chemistry-pyq.html') 

def sem2mathpyqs(request):
    return render(request, '../templates/sem2-math-pyq.html')  

def sem2csbasicspyqs(request):
    return render(request, '../templates/sem2-cs-basics-pyq.html')

def sem3mechanicspyqs(request):
    return render(request, '../templates/sem3-mechanics-pyq.html') 

def sem3organicchempyqs(request):
    return render(request, '../templates/sem3-organic-chem-pyq.html')
       
def sem3discretemathpyqs(request):
    return render(request, '../templates/sem3-discrete-math-pyq.html')  

def sem3introtocomputingpyqs(request):
    return render(request, '../templates/sem3-intro-to-computing-pyq.html')

def sem4electromagnetismpyqs(request):
    return render(request, '../templates/sem4-electromagnetism-pyq.html')

def sem4physicalchempyqs(request):
    return render(request, '../templates/sem4-physical-chem-pyq.html')  

def sem4linearalgebrapyqs(request):
    return render(request, '../templates/sem4-linear-algebra-pyq.html')

def sem4datastructurespyqs(request):
    return render(request, '../templates/sem4-data-structures-pyq.html') 

def sem5quantummechanicspyqs(request):
    return render(request, '../templates/sem5-quantum-mechanics-pyq.html')

def sem5inorganicchempyqs(request):
    return render(request, '../templates/sem5-inorganic-chem-pyq.html') 

def sem5dbmspyqs(request):
    return render(request, '../templates/sem5-dbms-pyq.html') 

def sem5ospyqs(request):
    return render(request, '../templates/sem5-os-pyq.html') 

def sem6relativitypyqs(request):
    return render(request, '../templates/sem6-relativity-pyq.html') 

def sem6thermodynamicspyqs(request):
    return render(request, '../templates/sem6-thermodynamics-pyq.html') 

def sem6compilerdesignpyqs(request):
    return render(request, '../templates/sem6-compiler-design-pyq.html')

def sem6softwareengineeringpyqs(request):
    return render(request, '../templates/sem6-software-engineering-pyq.html')

def sem7particlephysicspyqs(request):
    return render(request, '../templates/sem7-particle-physics-pyq.html') 

def sem7biochemistrypyqs(request):
    return render(request, '../templates/sem7-biochemistry-pyq.html') 

def sem7advanceddspyqs(request):
    return render(request, '../templates/sem7-advanced-ds-pyq.html')

def sem7aipyqs(request):
    return render(request, '../templates/sem7-ai-pyq.html') 

def sem8astrophysicspyqs(request):
    return render(request, '../templates/sem8-astrophysics-pyq.html') 

def sem8appliedchemistrypyqs(request):
    return render(request, '../templates/sem8-applied-chemistry-pyq.html')

def sem8mlpyqs(request):
    return render(request, '../templates/sem8-ml-pyq.html') 

def sem8cloudcomputingpyqs(request):
    return render(request, '../templates/sem8-cloud-computing-pyq.html')










#notes 
def subjects_btech(request):
    return render(request, '../templates/subjects-btech.html')
def subjects_bca(request):
    return render(request, '../templates/subjects-bca.html')
def subjects_bcom(request):
    return render(request, '../templates/subjects-bcom.html')
def subjects_bba(request):
    return render(request, '../templates/subjects-bba.html')
def subjects_mba(request):
    return render(request, '../templates/subjects-mba.html')

def notes(request):
    return rendassignmenter(request, '../templates/notes.html')

def resources_page(request, course, subject):
    with open('home/resources.json') as f:
        data = json.load(f)
    course_data = data.get(course.lower(), {})
    resources = course_data.get(subject.lower(), {'notes': [], 'videos': [], 'playlists': []})

    return render(request, 'notes.html', {'course': course, 'subject': subject, 'resources': resources})
