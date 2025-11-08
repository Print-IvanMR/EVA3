from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    # auth (login/logout) usando vistas genéricas
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:login'), name='logout'),

    # pacientes
    path('pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
    path('pacientes/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', views.PacienteDeleteView.as_view(), name='paciente_delete'),

    # cuidadores
    path('cuidadores/', views.CuidadorListView.as_view(), name='cuidador_list'),
    path('cuidadores/nuevo/', views.CuidadorCreateView.as_view(), name='cuidador_create'),
    path('cuidadores/<int:pk>/editar/', views.CuidadorUpdateView.as_view(), name='cuidador_update'),
    path('cuidadores/<int:pk>/eliminar/', views.CuidadorDeleteView.as_view(), name='cuidador_delete'),

    # medicamentos
    path('medicamentos/', views.MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamentos/nuevo/', views.MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamentos/<int:pk>/editar/', views.MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamentos/<int:pk>/eliminar/', views.MedicamentoDeleteView.as_view(), name='medicamento_delete'),

    # prescripciones
    path('prescripciones/', views.PrescripcionListView.as_view(), name='prescripcion_list'),
    path('prescripciones/nuevo/', views.PrescripcionCreateView.as_view(), name='prescripcion_create'),
    path('prescripciones/<int:pk>/editar/', views.PrescripcionUpdateView.as_view(), name='prescripcion_update'),
    path('prescripciones/<int:pk>/eliminar/', views.PrescripcionDeleteView.as_view(), name='prescripcion_delete'),

    # horarios
    path('horarios/', views.HorarioListView.as_view(), name='horario_list'),
    path('horarios/nuevo/', views.HorarioCreateView.as_view(), name='horario_create'),
    path('horarios/<int:pk>/eliminar/', views.HorarioDeleteView.as_view(), name='horario_delete'),

    # registros
    path('registros/', views.RegistroListView.as_view(), name='registro_list'),
    path('registros/nuevo/', views.RegistroCreateView.as_view(), name='registro_create'),
    path('registros/<int:pk>/eliminar/', views.RegistroDeleteView.as_view(), name='registro_delete'),

    # relaciones paciente-cuidador
    path('pacientecuidadores/', views.PacienteCuidadorListView.as_view(), name='pacientecuidador_list'),
    path('pacientecuidadores/nuevo/', views.PacienteCuidadorCreateView.as_view(), name='pacientecuidador_create'),
]
