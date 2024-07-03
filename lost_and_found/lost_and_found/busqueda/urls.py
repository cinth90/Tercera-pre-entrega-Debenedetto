from django.urls import path, include
from busqueda.views import *

urlpatterns = [
   path('', home, name="home"),
    path('ilost/', ilost, name="ilost"),
    path('ifound/', ifound, name="ifound"),
    #fomularios
     path('lostForm/', lostForm, name="lostForm"), # URL para el formulario de perdido
                                                    # URL para la vista de detalle del ítem perdido
    path('foundForm/', foundForm, name="foundForm"), # URL para el formulario de encontrado
    path('found/<int:pk>/', foundDetail, name='found_detail'),# URL para la vista de detalle del ítem encontrado
    
    #buscar
    path('buscarItem/', buscarItem, name="buscarItem"),
    path('encontrarItem/', encontrarItem, name="encontrarItem"),
    
    #Acerca de mi
    path('aboutme/', aboutme, name= "aboutme"),
   
    
    
    
    path('leerFound', leerFound, name = "LeerFound"),
    ]

