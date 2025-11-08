from django import forms
from django.core.exceptions import ValidationError
from .models import Paciente, Cuidador, Medicamento, Prescripcion, HorarioAdministracion, RegistroToma, PacienteCuidador
import datetime

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['rut','nombre','apellido','fecha_nacimiento','telefono','direccion','alergias']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date'}),
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not rut:
            raise ValidationError("RUT requerido")
        if len(rut) < 6:
            raise ValidationError("RUT demasiado corto")
        return rut

class CuidadorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['codigo','nombre','presentacion','descripcion','stock','precio']

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise ValidationError("el stock no puede ser negativo")
        return stock

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise ValidationError("Precio no puede ser negativo.")
        return precio

class PrescripcionForm(forms.ModelForm):
    class Meta:
        model = Prescripcion
        fields = ['paciente','medicamento','dosis','frecuencia','inicio','fin','instrucciones']
        widgets = {
            'inicio': forms.DateInput(attrs={'type':'date'}),
            'fin': forms.DateInput(attrs={'type':'date'}),
        }

    def clean(self):
        cleaned = super().clean()
        inicio = cleaned.get('inicio')
        fin = cleaned.get('fin')
        if inicio and fin and fin < inicio:
            raise ValidationError("la fecha fin no puede ser anterior a la fecha inicio")
        return cleaned

class HorarioForm(forms.ModelForm):
    class Meta:
        model = HorarioAdministracion
        fields = ['prescripcion','hora','dia_semana']
        widgets = {'hora': forms.TimeInput(attrs={'type':'time'})}

class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroToma
        fields = ['horario','cuidador','realizado','observaciones']

class PacienteCuidadorForm(forms.ModelForm):
    class Meta:
        model = PacienteCuidador
        fields = ['paciente','cuidador','encargado_actual']
