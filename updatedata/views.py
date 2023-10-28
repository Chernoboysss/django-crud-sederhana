from django.shortcuts import render,redirect,get_object_or_404
from mahasiswa.models import Data_mahasiswa
from insertdata.forms import BiodataMhs

# Create your views here.

def update(request,npm):
    obj = get_object_or_404(Data_mahasiswa,npm = npm)
    
    form = BiodataMhs(request.POST or None,instance = obj) 
    if form.is_valid():
        form.save()
        return redirect("/")
    
    data = {
        'mhs':obj,
    }
    return render(request,'editdata.html',data)