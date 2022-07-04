from django.shortcuts import redirect, render
from .models import todo
# Create your views here.

def index(request):
    if request.method == 'POST':
        new_todo = todo(title = request.POST['title'])
        new_todo.save()
    todo2 = todo.objects.all()
    return render(request, 'index.html', {'todos': todo2})

def delete(request, pk):
    todo1 = todo.objects.get(id=pk)
    todo1.delete()
    return redirect('/')
