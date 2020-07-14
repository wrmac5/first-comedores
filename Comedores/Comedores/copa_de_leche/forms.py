from django import forms

class formularioIngresoEsc(forms.Form):
    
    escuela = forms.CharField()
    cue = forms.CharField()
    delegacion = forms.CharField()
    localidad = forms.CharField()
    nivel = forms.CharField()
    modalidad = forms.CharField()
    nro_cuenta = forms.CharField()
    resp = forms.CharField()
    resp_dni = forms.CharField()
    sub_resp = forms.CharField()
    sub_resp_dni = forms.CharField()
    reso = forms.CharField()
