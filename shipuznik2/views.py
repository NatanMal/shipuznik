from django.shortcuts import render
from .models import Worker,Skills,User,Project
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def registration(request):
    if request.method == "GET":
        skills = Skills.objects.all() 
        return render(request, "registration.html", {"skills": skills})

    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        city = request.POST["city"]
        type =request.POST["type"]
        password = request.POST["password"]
        skills = Skills.objects.all()
        if type == "worker":
            worker = Worker(name = name, phone = phone, email = email, city = city, password = password)
            worker.save()
            #Skills.objects.get(skill_name=skill).workers.add(worker) adding a skill while registrating
            return render(request, "registration.html",{"skills": skills})
        if type == "user":
            user = User(name = name, phone = phone, city = city, password = password)
            user.save()
            return render(request, "registration.html",{"skills": skills})

def show(request):
    if request.method == "GET":
        worker = Worker.objects.all()
    return render(request, "show.html", {"worker":  worker})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        type = request.POST["type"]
        if type == "worker":   
            input_name = Worker.objects.filter(name = name ).values_list('password', flat = True)
            print("hey")
            print(name)
            print(input_name[0])
            print(password)
            print("check check")
            if password == input_name[0]:
                request.session['username'] = request.POST["name"]
                return HttpResponse("session created a worker is logged in")
            else:
                return HttpResponse("a worker is not authorized")
        elif type == "user" :
            input_name = User.objects.filter(name = name ).values_list('password', flat = True)
            print(input_name[0])
            print(password)
            print("check check")
            if password == input_name[0]:
                request.session['username'] = request.POST["name"]
                return HttpResponse("session created an user is logged in")
            else:
                return HttpResponse(" an user is not authorized")


def profile(request):
    if request.method == "GET":
        skills = Skills.objects.all()
        return render(request, "profile.html",{"skills": skills})
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        skill = request.POST["skill_id"]
        user  = User.objects.get(name = request.session['username']).values('id')
        worker = 1 #change it in the future
        skills = Skills.objects.all()
        Project.objects.create(name = name, description = description,
        skill_id_id = skill, user_id_id = user, worker_id_id = worker)
        return render(request, "profile.html",{"skills": skills})
    

def search(request):
    if request.method == "GET":
        return render(request, "search.html")
    if request.method == "POST":
        query = request.POST["q"]
        results = Worker.objects.filter(
        Q(name__icontains=query) | 
        Q(email__icontains=query) | 
        Q(city__icontains=query)
    )
    return render(request, "search.html", {"results": results})













