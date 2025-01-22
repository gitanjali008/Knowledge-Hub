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
    return render(request, '../templates/assignments/assignment.html')

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
    return render(request, '../templates/pyqs/btech pyqs/btech.html')
def bba(request):
    return render(request, '../templates/pyqs/bba pyqs/bba.html')
def mba(request):
    return render(request, '../templates/pyqs/mba pyqs/mba.html')
def bsc(request):
    return render(request, '../templates/bsc.html')
def mca(request):
    return render(request, '../templates/pyqs/mca pyqs/mca.html')
def mcom(request):
    return render(request, '../templates/mcom.html')
def bcom(request):
    return render(request, '../templates/bcom.html')
def bca(request):
    return render(request, '../templates/pyqs/bca pyqs/bca.html')
def btech_assignment(request):
    return render(request, '../templates/assignments/btech_assignment.html')    

def bba_assignment(request):
    return render(request, '../templates/assignments/bba_assignment.html')    

def bca_assignment(request):
    return render(request, '../templates/assignments/bca_assignment.html')    

def bcom_assignment(request):
    return render(request, '../templates/assignments/bcom_assignment.html')    
def mcom_assignment(request):
    return render(request, '../templates/assignments/mcom_assignment.html')    
                   



#previous year question paper 

def sem1mathpyqs(request):
    return render(request, '/templates/pyqs/btech pyqs/sem1-math-pyq.html')

def sem1physicspyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem1-physics-pyq.html')

def sem1ecepyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem1-ece-pyq.html')

def sem2mathpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem2-math-pyq.html')  

def sem2chemistrypyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem2-chemistry-pyq.html') 

def sem2evspyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem2-evs-pyq.html') 

def sem3OOPSpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem3-OOPS-pyq.html') 

def sem3dspyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem3-ds-pyq.html') 

def sem3digitallogicpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem3-digital-logic-pyq.html')

def sem4javapyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem4-java-pyq.html')  

def sem4micropyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem4-micro-pyq.html')

def sem4Automatapyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem4-Automata-pyq.html') 

def sem5mlpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem5-ml-pyq.html')  

def sem5databasepyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem5-database-pyq.html') 

def sem5ospyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem5-os-pyq.html')  

def sem6compilerpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem6-compiler-pyq.html') 

def sem6sepyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem6-se-pyq.html')  

def sem6networksecuritypyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem6-network-security-pyq.html') 

def sem7Softpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem7-soft-pyq.html')   

def sem7bipyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem7-bi-pyq.html') 

def sem7cgpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem7-cg-pyq.html') 

def sem8ccpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem8-cc-pyq.html') 

def sem8mbpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem8-mb-pyq.html') 

def sem8dmpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem8-dm-pyq.html') 

def sem1physicspyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem1-physics-pyq.html') 

def sem1chemistrypyqs(request):
    return render(request, '../templates/sem1-chemistry-pyq.html')

def sem1mathpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem1-math-pyq.html')  

def sem1englishpyqs(request):
    return render(request, '../templates/sem1-english-pyq.html') 

def sem2physicspyqs(request):
    return render(request, '../templates/sem2-physics-pyq.html') 

def sem2chemistrypyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem2-chemistry-pyq.html') 

def sem2mathpyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem2-math-pyq.html')  

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
    return render(request, '../templates/pyqs/btech pyqs/sem5-database-pyq.html') 

def sem5ospyqs(request):
    return render(request, '../templates/pyqs/btech pyqs/sem5-os-pyq.html') 

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

def sem1computerfundamental(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem1-computerfundamental-pyq.html') 
def sem1maths(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem1-maths-pyq.html') 
def sem1programminginc(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem1-programming.pyq.html') 
def sem2maths(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem2-math-pyq.html') 
def sem2datastructure(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem2-datastructure-pyq.html') 
def sem2dbmspyqs(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem2-dbms-pyq.html') 
def sem3os(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem3-os-pyq.html') 
def sem3oop(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem3-oop-pyq.html') 
def sem3computernetwork(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem3-computernetwork-pyq.html') 
def sem3softwareengineering(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem3-softwareengineering-pyq.html') 
def sem4dda(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem4-dda-pyq.html') 
def sem4softwaredevelopment(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem4-softwaredevelopment-pyq.html') 
def sem4computerarchietecture(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem4-computerarchietecture-pyq.html') 
def sem4evs(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem4-evs-pyq.html') 
def sem5webtech(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem5-webtechnologies-pyq.html') 
def sem5mobilecomputing(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem5-mobiletech-pyq.html') 
def sem5networksecurity(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem5-networksequrity-pyq.html') 
def sem5ai(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem5-AI-pyq.html') 
def sem6bigdataanalysis(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem6-bigdata-pyq.html') 
def sem6cloudcomputing(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem6-cloudcomputing-pyq.html') 
def sem6projectmanagement(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem6-projectmanagement-pyq.html') 
def sem6datascience(request):
    return render(request, '../templates/pyqs/bca pyqs/bca-sem6-datascience-pyq.html') 

def bbasem1buisnessmaths(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem1-buisnessmathe-pyq.html') 
def bbasem1finalcialaccounting(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem1-finacialacco-pyq.html') 
def bbasem1microeco(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem1-microeconomics-pyq.html') 
def bbasem1principlemanagement(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem1-priciplemanagemenet-pyq.html') 
def bbasem2buisnesscommunication(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem2-businnescommunication-pyq.html') 
def bbasem2humanresource(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem2-humanresource-pyq.html') 
def bbasem2macroeconomics(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem2-macroeconomics-pyq.html') 
def bbasem2origanization(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem2-organizationalbehavior-pyq.html') 
def bbasem3buisnesslaw(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem3-businesslaw-pyq.html') 
def bbasem3corporateaccoun(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem3-corporateaccounting-pyq.html') 
def bbasem3managementaccount(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem3-managementaccounting-pyq.html') 
def bbasem3marketing(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem3-marketing-pyq.html') 
def bbasem4businesseco(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem4-businesseconomics-pyq.html') 
def bbasem4costaccounting(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem4-costaccounting-pyq.html') 
def bbasem4production(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem4-production-pyq.html') 
def bbasem4quantitative(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem4-quantitativetechniques-pyq.html') 
def bbasem5enterpreneuship(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem5-enterpreneurship-pyq.html') 
def bbasem5internationalbusiness(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem5-internationalbusiness-pyq.html') 
def bbasem5investmentmanagement(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem5-investmentmanagement-py.html') 
def bbasem5strategicmanagement(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem5-startegicmanagement-pyq.html') 
def bbasem6finacialmanagement(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem6-finacialmanagement-pyq.html') 
def bbasem6marketing(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem6-marketingresearch-pyq.html') 
def bbasem6organization(request):
    return render(request, '../templates/pyqs/bba pyqs/bba-sem6-organizationaldevelopment-pyq.html') 

def sem1managerialeconomicspyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem1-managerial-economicspyq.html')
def sem1organizationalbehaviorpyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem1-oraganizationalbehaviourpyq.html')
def sem1accountingformanagerspyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem1-accoutingformanagerpyq.html')
def sem1quantitativemethodspyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem1-quantitativemethodspyq.html')
def sem2financialmanagementpyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem2-finacialmanagement-pyq.html')
def sem2marketingmanagementpyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem2-marketingmanagement-pyq.html')
def sem2operationsmanagementpyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem2-operationmanagement-pyq.html')
def sem2hrmpyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem2-humanresourcemanagemenet-pyq.html')
def sem3businessresearchmethodspyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem3-businessresearchmethods-pyq.html')
def sem3strategicmanagementpyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem3-strategicmanagement-pyq.html')
def sem3internationalbusinesspyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem3-internationalbusiness-pyq.html')
def sem3businessethicspyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem3-businessethics-pyq.html')
def sem4corporategovernancepyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem4-corporategovernance-pyq.html')
def sem4projectmanagementpyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem4-projectmanagement-pyq.html')
def sem4investmentmanagementpyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem4-investmentmanagemenet-pyq.html')
def sem4entrepreneurshippyqs(request):
    return render(request, '../templates/pyqs/mba pyqs/mba-sem4-entrepreneurship-pyq.html')












#notes 
def subjects_btech(request):
    return render(request, '../templates/btech-notes.html')
def subjects_bca(request):
    return render(request, '../templates/bca-notes.html')
def subjects_bcom(request):
    return render(request, '../templates/bcom-notes.html')
def subjects_bba(request):
    return render(request, '../templates/bba-notes.html')
def subjects_mba(request):
    return render(request, '../templates/mba-notes.html')

def notes(request):
    return rendassignmenter(request, '../templates/notes.html')

def resources_page(request, course, subject):
    with open('home/resources.json') as f:
        data = json.load(f)
    course_data = data.get(course.lower(), {})
    resources = course_data.get(subject.lower(), {'notes': [], 'videos': [], 'playlists': []})

    return render(request, 'notes.html', {'course': course, 'subject': subject, 'resources': resources})
