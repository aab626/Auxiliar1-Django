from django.shortcuts import render, redirect

# Create your views here.
from todoapp.models import Tarea
from categorias.models import Categoria

def tareas(request):
    mis_tareas = Tarea.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'GET':
        return render(request, "todoapp/index.html", {"tareas": mis_tareas, "categorias": categorias})
    
    if request.method == 'POST':
        if 'taskAdd' in request.POST:
            titulo = request.POST['titulo']
            
            nombre_categoria = request.POST['selector_categoria']
            categoria = Categoria.objects.get(nombre=nombre_categoria)

            contenido = request.POST['contenido']

            nueva_tarea = Tarea(titulo=titulo, contenido=contenido, categoria=categoria)
            nueva_tarea.save()

            return redirect('/tareas')

