from django.shortcuts import render
from personas.models import Persona

# Create your views here.
def bienvenido(request):
    nro_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'nro_personas': nro_personas, 'personas': personas})
