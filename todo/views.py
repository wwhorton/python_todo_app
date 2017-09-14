from django.shortcuts import render, reverse, redirect
from .models import ToDo

# Create your views here.


def index(request):
    to_do_list = ToDo.objects.order_by('-due_date')
    context = {'to_do_list': to_do_list}
    return render(request, 'todo/index.html', context)


def add(request):
    text = request.POST['todo_text']
    due = request.POST['due_date']
    new_task = ToDo(todo_text=text, due_date=due)
    new_task.save()
    return redirect(reverse('index'))


def complete(request):
    todo = ToDo.objects.get(id=request.POST['todo_id'])
    todo.complete_task()
    todo.save()
    return redirect(reverse('index'))
