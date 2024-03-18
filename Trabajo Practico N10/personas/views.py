from django.shortcuts import render, redirect
from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio

# Create your views here.
def detallePersonas(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona':persona})

def nuevaPersona(request):
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})

def editarPersona(request, id):
    persona = Persona.objects.get(pk=id)
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona':formaPersona})

def eliminarPersona(request, id):
    persona = Persona.objects.get(pk=id)
    if persona:
        persona.delete()
    return redirect('index')

def nuevoDomicilio(request):
    if request.method == "POST":
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm()
    return render(request, 'personas/domicilio.html', {'formaDomicilio': formaDomicilio})
