from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template, Context, loader
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #para class
from django.contrib.auth.decorators import login_required #para funciones


#inicio
def home(request):
    return render(request, 'busqueda/index.html')

#about me
def aboutme(request):
    return render(request, "busqueda/aboutme.html")

#___ Formularios
# formulario para ingresar item que alguien perdió
@login_required
def lostForm(request):
    if request.method == "POST":
        miForm = LostForm(request.POST, request.FILES)
        if miForm.is_valid():
            lost_name_booking = miForm.cleaned_data.get("name_booking")
            lost_room_number = miForm.cleaned_data.get("room_number")
            lost_email = miForm.cleaned_data.get("email")
            lost_when = miForm.cleaned_data.get("when")
            lost_what = miForm.cleaned_data.get("what")
            lost_where = miForm.cleaned_data.get("where")
            lost_color = miForm.cleaned_data.get("color", "") #COLOR O VACIO: NO ES OBLIGATORIO
            lost_model = miForm.cleaned_data.get("model", "")
            lost_size = miForm.cleaned_data.get("size", "")
            lost_description = miForm.cleaned_data.get("description", "")
            lost_photo = miForm.cleaned_data.get("photo", "")
            lost = Ilost(name_booking =lost_name_booking,
                         room_number =lost_room_number,
                         email =lost_email,
                         when =lost_when,
                         what =lost_what,
                         where=lost_where,
                         color=lost_color,
                         model=lost_model,
                         size=lost_size,
                         description=lost_description,
                         photo = lost_photo)
            lost.save()
            return redirect('lost_detail', pk=lost.pk) #SOLO QUIERO QUE MUESTRE EL ITEM RECIEN INGRESADO
    else:
        miForm = LostForm()
    
    return render(request, "busqueda/lostForm.html", {"form": miForm})

@login_required
def lostDetail(request, pk):
    lost = get_object_or_404(Ilost, pk=pk)
    return render(request, 'busqueda/lost_detail.html', {'lost': lost})

# formulario para ingresar item que alguien encontró
@login_required
def foundForm(request):
    if request.method == "POST":
        miForm = FoundForm(request.POST, request.FILES)

        if miForm.is_valid():
            found_when = miForm.cleaned_data.get("when")
            found_what = miForm.cleaned_data.get("what")
            found_where = miForm.cleaned_data.get("where")
            found_color = miForm.cleaned_data.get("color", "") #COLOR O VACIO: NO ES OBLIGATORIO
            found_model = miForm.cleaned_data.get("model", "")
            found_size = miForm.cleaned_data.get("size", "")
            found_description = miForm.cleaned_data.get("description", "")
            found_photo = miForm.cleaned_data.get("photo", "")
    
            found = Ifound(when =found_when,
                           what =found_what,
                           where=found_where,
                           color=found_color,
                           model=found_model,
                           size=found_size,
                           description= found_description,
                           photo = found_photo)
            found.save()
            return redirect('found_detail', pk=found.pk) #SOLO QUIERO QUE MUESTRE EL ITEM RECIEN INGRESADO
    else:
        miForm = FoundForm()
    return render(request, "busqueda/foundForm.html", {"form": miForm})
@login_required   
def foundDetail(request, pk):
    found = get_object_or_404(Ifound, pk=pk)
    return render(request, 'busqueda/found_detail.html', {'found': found})

#buscar items en la base de datos
@login_required
def buscarItem(request):
    return render(request, "busqueda/buscar.html")

#funcion parar encontrar coincidencias en la base de datos
@login_required
def encontrarItem(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar'].strip()
        if patron:
            
            queryset = (
                Ifound.objects.filter(what__icontains=patron)
                | Ifound.objects.filter(where__icontains=patron)
                | Ifound.objects.filter(when__icontains=patron)
                | Ifound.objects.filter(color__icontains=patron)
                | Ifound.objects.filter(model__icontains=patron)
                | Ifound.objects.filter(size__icontains=patron)
            ).distinct()
            
            found = list(queryset)
        else:
            found = Ifound.objects.all()
    else:
        found = Ifound.objects.all()
            
    contexto = {'found': found}
    return render(request, "busqueda/found.html", contexto)

#Dejar testimonios
@login_required
def testimonial_create(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')  # Redirige a una página de agradecimiento
    else:
        form = TestimonialForm()

    return render(request, 'busqueda/testimonial_form.html', {'form': form})

def gracias(request):
    return render(request, 'busqueda/gracias.html')

# Login/ Logout(usamos CBV)

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username = usuario, password= clave) #Valida si el usuario y contraseña estan la base de dato
        if user is not None:  
            login(request, user)
            
            #_____ BUSCAR AVATAR
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url #si tiene avatar
            except:
                avatar = "media/avatares/default.png"                        #si no tiene avatar
            finally:
                request.session["avatar"] = avatar
            #__________________________
            return render(request, "busqueda/index.html")
        else: 
            return redirect(reverse_lazy('login'))  
                            
    else: 
        miForm = AuthenticationForm()
        
    return render(request, "busqueda/login.html", {"form": miForm})


#  Registracion de nuevo usuario
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return render(request, 'busqueda/singup_exito.html')  
        else:
            return render(request, "busqueda/registro.html", {"form": miForm})
    else:
        miForm = RegistroForm()
        
        return render(request, "busqueda/registro.html", {"form": miForm})   

# Edicion de perfil
@login_required
def editProfile(request):
    usuario = request.user
    if request.method =="POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario) #Carga los datos del usuario que esta logueado
    return render(request, "busqueda/editarPerfil.html", {"form": miForm})    


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "busqueda/cambiar_clave.html"
    success_url = reverse_lazy("home")

#Agregar AVATAR
  
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_______ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #_____________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #_________________________________________________
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "busqueda/agregarAvatar.html", {"form": miForm})    
    
#Formulario de contacto
@login_required
def contactar(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')  # Redirige a una página de agradecimiento
    else:
        form = ContactForm()

    return render(request, 'busqueda/contactar.html', {'form': form})

def gracias(request):
    return render(request, 'busqueda/gracias.html')