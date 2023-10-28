from django.shortcuts import render,redirect,get_object_or_404
from .forms import BiodataMhs

# Create your views here.
def insert(request):
    form = BiodataMhs(request.POST or None,request.FILES or None)
    if request.method == 'POST' :
        if form.is_valid():
            form.save()
            return redirect("/")
        pass
    
    return render(request,'insert.html')