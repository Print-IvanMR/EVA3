from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class Paciente(models.Model):
    rut = models.CharField('RUT', max_length=20, unique=True)
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    direccion = models.TextField(blank=True)
    alergias = models.TextField('Alergias/Observaciones', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"

    def get_absolute_url(self):
        return reverse('core:paciente_detail', args=[self.pk])


class Cuidador(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    parentesco = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Medicamento(models.Model):
    codigo = models.CharField('Código', max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    presentacion = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField(blank=True)
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

    def get_absolute_url(self):
        return reverse('core:medicamento_detail', args=[self.pk])


class Prescripcion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prescripciones')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT, related_name='prescripciones')
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100, help_text='ej: 1 cápsula cada 8 horas')
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)
    instrucciones = models.TextField(blank=True)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Prescripción: {self.paciente} - {self.medicamento}"

    def get_absolute_url(self):
        return reverse('core:prescripcion_detail', args=[self.pk])


class HorarioAdministracion(models.Model):
    prescripcion = models.ForeignKey(Prescripcion, on_delete=models.CASCADE, related_name='horarios')
    hora = models.TimeField()
    dia_semana = models.CharField(max_length=20, blank=True, help_text='Opcional: Lunes, Martes...')

    def __str__(self):
        return f"{self.prescripcion} @ {self.hora}"


class RegistroToma(models.Model):
    horario = models.ForeignKey(HorarioAdministracion, on_delete=models.CASCADE, related_name='registros')
    cuidador = models.ForeignKey(Cuidador, on_delete=models.SET_NULL, null=True, blank=True, related_name='registros')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    realizado = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.horario.prescripcion} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"


class PacienteCuidador(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente_cuidadores')
    cuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE, related_name='paciente_cuidadores')
    encargado_actual = models.BooleanField(default=False)

    class Meta:
        unique_together = ('paciente', 'cuidador')

    def __str__(self):
        return f"{self.cuidador} -> {self.paciente}"
