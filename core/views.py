from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Paciente, Cuidador, Medicamento, Prescripcion, HorarioAdministracion, RegistroToma, PacienteCuidador
from .forms import PacienteForm, CuidadorForm, MedicamentoForm, PrescripcionForm, HorarioForm, RegistroForm, PacienteCuidadorForm
from django.contrib import messages

# paciente CRUD
class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'pacientes/lista.html'
    context_object_name = 'pacientes'

class PacienteDetailView(LoginRequiredMixin, DetailView):
    model = Paciente
    template_name = 'pacientes/detail.html'

class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/formulario.html'
    success_url = reverse_lazy('core:paciente_list')
    def form_valid(self, form):
        messages.success(self.request, "Paciente creado correctamente.")
        return super().form_valid(form)

class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/formulario.html'
    success_url = reverse_lazy('core:paciente_list')
    def form_valid(self, form):
        messages.success(self.request, "Paciente actualizado correctamente.")
        return super().form_valid(form)

class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'pacientes/confirm_delete.html'
    success_url = reverse_lazy('core:paciente_list')

# cuidador CRUD 
class CuidadorListView(LoginRequiredMixin, ListView):
    model = Cuidador
    template_name = 'cuidadores/lista.html'
    context_object_name = 'cuidadores'

class CuidadorCreateView(LoginRequiredMixin, CreateView):
    model = Cuidador
    form_class = CuidadorForm
    template_name = 'cuidadores/formulario.html'
    success_url = reverse_lazy('core:cuidador_list')

class CuidadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Cuidador
    form_class = CuidadorForm
    template_name = 'cuidadores/formulario.html'
    success_url = reverse_lazy('core:cuidador_list')

class CuidadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Cuidador
    template_name = 'cuidadores/confirm_delete.html'
    success_url = reverse_lazy('core:cuidador_list')

# medicamento CRUD 
class MedicamentoListView(LoginRequiredMixin, ListView):
    model = Medicamento
    template_name = 'medicamentos/lista.html'
    context_object_name = 'medicamentos'

class MedicamentoCreateView(LoginRequiredMixin, CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'medicamentos/formulario.html'
    success_url = reverse_lazy('core:medicamento_list')
    def form_valid(self, form):
        messages.success(self.request, "Medicamento creado.")
        return super().form_valid(form)

class MedicamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'medicamentos/formulario.html'
    success_url = reverse_lazy('core:medicamento_list')

class MedicamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicamento
    template_name = 'medicamentos/confirm_delete.html'
    success_url = reverse_lazy('core:medicamento_list')

# prescripcion CRUD 
class PrescripcionListView(LoginRequiredMixin, ListView):
    model = Prescripcion
    template_name = 'prescripciones/lista.html'
    context_object_name = 'prescripciones'

class PrescripcionCreateView(LoginRequiredMixin, CreateView):
    model = Prescripcion
    form_class = PrescripcionForm
    template_name = 'prescripciones/formulario.html'
    success_url = reverse_lazy('core:prescripcion_list')

class PrescripcionUpdateView(LoginRequiredMixin, UpdateView):
    model = Prescripcion
    form_class = PrescripcionForm
    template_name = 'prescripciones/formulario.html'
    success_url = reverse_lazy('core:prescripcion_list')

class PrescripcionDeleteView(LoginRequiredMixin, DeleteView):
    model = Prescripcion
    template_name = 'prescripciones/confirm_delete.html'
    success_url = reverse_lazy('core:prescripcion_list')

# horarios 
class HorarioListView(LoginRequiredMixin, ListView):
    model = HorarioAdministracion
    template_name = 'horarios/lista.html'
    context_object_name = 'horarios'

class HorarioCreateView(LoginRequiredMixin, CreateView):
    model = HorarioAdministracion
    form_class = HorarioForm
    template_name = 'horarios/formulario.html'
    success_url = reverse_lazy('core:horario_list')

class HorarioDeleteView(LoginRequiredMixin, DeleteView):
    model = HorarioAdministracion
    template_name = 'horarios/confirm_delete.html'
    success_url = reverse_lazy('core:horario_list')

#  registros de toma 
class RegistroListView(LoginRequiredMixin, ListView):
    model = RegistroToma
    template_name = 'registros/lista.html'
    context_object_name = 'registros'

class RegistroCreateView(LoginRequiredMixin, CreateView):
    model = RegistroToma
    form_class = RegistroForm
    template_name = 'registros/formulario.html'
    success_url = reverse_lazy('core:registro_list')

class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    model = RegistroToma
    template_name = 'registros/confirm_delete.html'
    success_url = reverse_lazy('core:registro_list')

# paciente - cuidador
class PacienteCuidadorListView(LoginRequiredMixin, ListView):
    model = PacienteCuidador
    template_name = 'pacientecuidadores/lista.html'
    context_object_name = 'relaciones'

class PacienteCuidadorCreateView(LoginRequiredMixin, CreateView):
    model = PacienteCuidador
    form_class = PacienteCuidadorForm
    template_name = 'pacientecuidadores/formulario.html'
    success_url = reverse_lazy('core:pacientecuidador_list')
