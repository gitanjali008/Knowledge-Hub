from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin',admin.site.urls),
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
   path('contact/', views.contact, name='contact'),
    path("faculty/", views.faculty, name='faculty'),
    path("course_outline/", views.course_outline, name='course_outline'),
    path("practice/index/", views.index, name='index'),
    path("course_outline/index/", views.index, name='index'),
    path("faculty/index/", views.index, name='index'),
]
