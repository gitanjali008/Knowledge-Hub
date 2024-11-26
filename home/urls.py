from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin',admin.site.urls),
    path("about/", views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('', views.login_view, name='login'), 
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("faculty/", views.faculty, name='faculty'),
     path("pyq/", views.pyq, name='pyq'),
    path("course_outline/", views.course_outline, name='course_outline'),
    path("practice/index/", views.index, name='index'),
    path("course_outline/index/", views.index, name='index'),
    path("faculty/index/", views.index, name='index'),
     path("book/", views.book, name='book'),
]
