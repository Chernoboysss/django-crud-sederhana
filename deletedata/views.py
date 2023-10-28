from django.shortcuts import render,redirect,get_object_or_404
from mahasiswa.models import Data_mahasiswa
from insertdata.forms import BiodataMhs


# Create your views here.
def delete(request,npm):
    dt = Data_mahasiswa.objects.get(npm = npm)
    dt.delete()
    
    return redirect("/")