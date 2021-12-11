from django.urls import path
from AppCoder import views

urlpatterns = [
      path('', views.inicio, name='Inicio'),
      path('crear_usuario/', views.crear_usuario, name='link1'),
      path('buscar/', views.buscar, name='buscar'),
      path('link3/', views.link3, name='link3'),
      path('turnos/', views.turnos, name='turnos'),
]