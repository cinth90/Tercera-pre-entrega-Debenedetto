from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template, Context, loader
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'busqueda/index.html')

#about me
def aboutme(request):
    return render(request, "busqueda/aboutme.html")


def ilost(request):
    contexto = {"lost": Ilost.objects.all()}
    return render(request, "busqueda/lost.html", contexto)



def ifound(request):
    contexto = {"found": Ifound.objects.all()}
    return render(request, "busqueda/found.html", contexto)

#___ Formularios
def lostForm(request):
    if request.method == "POST":
        miForm = LostForm(request.POST)
        if miForm.is_valid():
            lost_when = miForm.cleaned_data.get("when")
            lost_what = miForm.cleaned_data.get("what")
            lost_where = miForm.cleaned_data.get("where")
            lost_color = miForm.cleaned_data.get("color")
            lost_model = miForm.cleaned_data.get("model")
            lost_size = miForm.cleaned_data.get("size")
    
            lost = Ilost(when =lost_when, what =lost_what, where=lost_where, color=lost_color,model=lost_model, size=lost_size)
            lost.save()
            contexto = {"lost": Ilost.objects.all() }
            return render(request, "busqueda/lost.html", contexto)
    else:
        miForm = LostForm()
    
    return render(request, "busqueda/lostForm.html", {"form": miForm})

def foundForm(request):
    if request.method == "POST":
        miForm = FoundForm(request.POST)
        if miForm.is_valid():
            found_when = miForm.cleaned_data.get("when")
            found_what = miForm.cleaned_data.get("what")
            found_where = miForm.cleaned_data.get("where")
            found_color = miForm.cleaned_data.get("color", "") #COLOR O VACIO: NO ES OBLIGATORIO
            found_model = miForm.cleaned_data.get("model", "")
            found_size = miForm.cleaned_data.get("size", "")
    
            found = Ifound(when =found_when,
                           what =found_what,
                           where=found_where,
                           color=found_color,
                           model=found_model,
                           size=found_size)
            found.save()
            return redirect('found_detail', pk=found.pk) #SOLO QUIERO QUE MUESTRE EL ITEM RECIEN INGRESADO
    else:
        miForm = FoundForm()
    return render(request, "busqueda/foundForm.html", {"form": miForm})
    
def foundDetail(request, pk):
    found = get_object_or_404(Ifound, pk=pk)
    return render(request, 'busqueda/found_detail.html', {'found': found})

#buscar items en la base de datos

def buscarItem(request):
    return render(request, "busqueda/buscar.html")

#funcion parar encontrar coincidencias en la base de datos

def encontrarItem(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar'].strip()  # Get the search query
        if patron:
            # Perform case-insensitive partial matches on different fields
            queryset = (
                Ifound.objects.filter(what__icontains=patron)
                | Ifound.objects.filter(where__icontains=patron)
                | Ifound.objects.filter(when__icontains=patron)
                | Ifound.objects.filter(color__icontains=patron)
                | Ifound.objects.filter(model__icontains=patron)
                | Ifound.objects.filter(size__icontains=patron)
            ).distinct()  # Ensure distinct results
            
            found = list(queryset)  # Convert queryset to list for iteration
        else:
            found = Ifound.objects.all()  # Fetch all items if no search query provided
    else:
        found = Ifound.objects.all()  # Fetch all items if no 'buscar' parameter
    
    contexto = {'found': found}
    return render(request, "busqueda/found.html", contexto)

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
