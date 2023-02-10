from django.shortcuts import render
from .models import Worker,Skills

# Create your views here.

def home(request):
    if request.method == "GET":
        skills = Skills.objects.all() 
        return render(request, "index.html", {"skills": skills})

    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        city = request.POST["city"]
        skill =request.POST["skill"]
        skills = Skills.objects.all()
        worker = Worker(name = name, phone = phone, email = email, city = city)
        worker.save()
        Skills.objects.get(skill_name=skill).workers.add(worker)
        return render(request, "index.html",{"skills": skills})

def show(request):
    if request.method == "GET":
        worker = Worker.objects.all()
    return render(request, "show.html", {"worker":  worker})






