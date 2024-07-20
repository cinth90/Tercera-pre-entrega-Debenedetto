from django.urls import path, include
from busqueda.views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name="home"),
    path('admin/', home, name="admin"),
  
   #fomulario items perdidos
    path('lostForm/', lostForm, name="lostForm"), # URL para el formulario de perdido
    path('lost/<int:pk>/', lostDetail, name='lost_detail'),# URL para la vista de detalle del ítem perdido cargado
    
    #formulario items encontradis
    path('foundForm/', foundForm, name="foundForm"), # URL para el formulario de encontrado
    path('found/<int:pk>/', foundDetail, name='found_detail'),# URL para la vista de detalle del ítem encontrado
    
  
   #buscar en la base de items encontrados
    path('buscarItem/', buscarItem, name="buscarItem"),
    path('encontrarItem/', encontrarItem, name="encontrarItem"),
    
   #Acerca de mi
    path('aboutme/', aboutme, name= "aboutme"),
   
   #Testimonios
    path('testimonial_create/', testimonial_create, name='testimonial_create'),
    path('gracias/', gracias, name='gracias'),
    
    #login/logout/ registracion
    path('login/', loginRequest, name='login'),
    path('logout/', LogoutView.as_view(template_name="busqueda/logout.html"), name="logout"),
    path('registro/', register, name='registro'),
    
    #Edicion de perfil / Avatar
    path('perfil/', editProfile, name='perfil'),
    path('<int:pk>/password/',CambiarClave.as_view() , name='cambiarClave'),
    path('agregar_avatar/', agregarAvatar, name='agregar_avatar'),
    
    #formulario de contacto
    path('contactar/', contactar, name='contactar'),
      
       
    ]

