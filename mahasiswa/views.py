from django.shortcuts import render
from .models import Data_mahasiswa

# Create your views here.
def index(request):
    hasil = Data_mahasiswa.objects.all()
    print(hasil)
    data = {
        'data' : hasil,
    }
    return render(request,'read.html',data)