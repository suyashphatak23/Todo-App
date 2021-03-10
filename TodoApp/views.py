from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def index(request):
    if request.method == "POST":

        new_todo_title = request.POST['title']
        if not new_todo_title or len(new_todo_title) < 3:
            return redirect('index')
        new_todo_content = request.POST['text']

        todo = Todo()
        todo.header = new_todo_title
        todo.content = new_todo_content
        todo.save()
        return redirect('index')

    todo = Todo.objects.all()
    incomplete = 0
    complete = 0
    for each in todo:
        if each.isCompleted:
            complete += 1
        else:
            incomplete += 1

    return render(request, 'index.html', {'todos':todo, 'incomplete_count': incomplete, 'completed_count': complete})


def delete(request, todo_id):
    if request.method == 'POST':

        if request.POST.get('delete'):
            todo = get_object_or_404(Todo, pk = todo_id)
            todo.delete()
            return redirect('index')

        if request.POST.get('complete'):
            todo = get_object_or_404(Todo, pk = todo_id)
            todo.isCompleted = True
            todo.save()
            return redirect('index')

        if request.POST.get('update'):
            return render(request, 'update.html', {'todo_id': todo_id})


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk = todo_id)
    todo.header = request.POST['header']
    todo.content = request.POST['content']
    todo.save()
    return redirect('index')
