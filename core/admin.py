from django.contrib import admin
from .models import Paciente, Cuidador, Medicamento, Prescripcion, HorarioAdministracion, RegistroToma, PacienteCuidador

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre','apellido','fecha_nacimiento')
    search_fields = ('rut','nombre','apellido')

@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','email')
    search_fields = ('nombre','apellido','telefono')

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','stock','precio')
    search_fields = ('codigo','nombre')
    list_filter = ('laboratorio',)

@admin.register(Prescripcion)
class PrescripcionAdmin(admin.ModelAdmin):
    list_display = ('paciente','medicamento','dosis','inicio','fin')
    list_filter = ('inicio',)
    search_fields = ('paciente__nombre','medicamento__nombre')

@admin.register(HorarioAdministracion)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('prescripcion','hora','dia_semana')

@admin.register(RegistroToma)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('horario','cuidador','fecha_hora','realizado')
    list_filter = ('realizado',)

@admin.register(PacienteCuidador)
class PacienteCuidadorAdmin(admin.ModelAdmin):
    list_display = ('paciente','cuidador','encargado_actual')
