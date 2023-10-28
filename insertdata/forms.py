from django import forms
from mahasiswa.models import Data_mahasiswa

class BiodataMhs(forms.ModelForm):
    class Meta:
        model = Data_mahasiswa
        fields = "__all__"
        error_massage = {
            'npm': {
                'required': 'NPM harus diisi',
            },
            'nama':{
                'max_length':'Nama tidak boleh lebih dari 50 karakter',
                'requiered' : 'Nama harus diisi'
                },
            'tgl_lahir' : {
                'requied' : 'Tanggal Harus diisi'
            },
            'alamat' : {
                'required' : 'harus diisi alamatnya broww'
            }
        }