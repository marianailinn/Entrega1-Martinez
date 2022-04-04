from django.urls import include, path
from AppCoder import views
from .views import agregarPersonas

urlpatterns = [
    path('', views.inicio),
    path('persona/',views.listar_Personas),
    path('personaFormulario/',views.personas,name="Persona"),
    path('agregapersona/', agregarPersonas),
]
