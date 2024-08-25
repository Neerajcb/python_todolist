# from django.shortcuts import render

# Create your views here.
# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# from .models import Task
# from .models import Task

# from django.shortcuts import render
# from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('/')

def update_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'status': 'success'})

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return JsonResponse({'status': 'success'})
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('/')
    
    return render(request, 'edit_task.html', {'task': task})



@csrf_exempt  # Use this if CSRF token is disabled, though not recommended in production
def toggle_completed(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        data = json.loads(request.body)
        task.completed = data['completed']
        task.save()
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'failed'}, status=400)
