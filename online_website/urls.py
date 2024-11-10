from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Knowledge Hub Admin"
admin.site.site_title = "Knowledge Hub Admin Portal"
admin.site.index_title = "Welcome to Knowledge Hub"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]


