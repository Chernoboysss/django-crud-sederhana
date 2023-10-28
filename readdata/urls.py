"""
URL configuration for readdata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mahasiswa import views
from insertdata import views as insert
from updatedata import views as update
from deletedata import views as delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="read"),
    path('insert',insert.insert,name ="insert"),
    path('updatedata/<str:npm>/',update.update,name="update"),
    path('deletedata/<str:npm>/',delete.delete,name="delete")
    
]
