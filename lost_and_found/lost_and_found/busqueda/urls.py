from django.urls import path, include
from busqueda.views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
   path('', home, name="home"),
    path('ilost/', ilost, name="ilost"),
    path('ifound/', ifound, name="ifound"),
   #fomularios
     path('lostForm/', lostForm, name="lostForm"), # URL para el formulario de perdido
                                                    # URL para la vista de detalle del ítem perdido
    path('foundForm/', foundForm, name="foundForm"), # URL para el formulario de encontrado
    path('found/<int:pk>/', foundDetail, name='found_detail'),# URL para la vista de detalle del ítem encontrado
    path('lost/<int:pk>/', lostDetail, name='lost_detail'),# URL para la vista de detalle del ítem perdido cargado
  
   #buscar
    path('buscarItem/', buscarItem, name="buscarItem"),
    path('encontrarItem/', encontrarItem, name="encontrarItem"),
    
   #Acerca de mi
    path('aboutme/', aboutme, name= "aboutme"),
   
   #Testimonios
    path('testimonial_create/', testimonial_create, name='testimonial_create'),
    path('gracias/', gracias, name='gracias'),
    
    #login/logout/ registracion
    path('login/', loginRequest, name='login'),
    path('logout/', LogoutView.as_view(template_name='busqueda/logout.html'), name='logout'),
    
    path('registro/', register, name='registro'),
    
    

   
    ]

