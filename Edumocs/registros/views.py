from django.shortcuts import render
from .models import Cursos 

# Create your views here.
def cursos(request):
    cursos=Cursos.objects.all()
    #Indicamos el lugar donde se renderizará el resultado de esta vista

    return render(request,"registros/cursos.html",{'cursos':cursos})

def catalogo(request):
    cursos=Cursos.objects.filter(titulo="Curso completo de Python 3 de la A a la Z - 2021 +50 horas!")
    #Indicamos el lugar donde se renderizará el resultado de esta vista

    return render(request,"registros/catalogo.html",{'cursos':cursos})