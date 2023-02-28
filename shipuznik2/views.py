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
                request.session['type'] = request.POST["type"]
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
                request.session['type'] = request.POST["type"]
                return HttpResponse("session created an user is logged in")
            else:
                return HttpResponse(" an user is not authorized")


def add_project(request):
    if request.method == "GET":
        print("fckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkc")
        skills = Skills.objects.all()
        workers = Worker.objects.all()
        return render(request, "add_project.html",{"skills": skills, "workers":workers})
    if request.method == "POST":
        print("sdlfjdslfsjflajs;dfjasdfkjaslfkjadslfkasdjflkasdjfalskfnalsdkfsadl")
        name = request.POST["name"]
        description = request.POST["description"]
        skill = request.POST["skill_id"]
        worker = request.POST["worker_id"]
        print(skill)
        user  = User.objects.filter(name=request.session['username']).values_list("id", flat=True).first()
        skills = Skills.objects.all()
        workers = Worker.objects.all()
        Project.objects.create(name = name, description = description,
        skill_id_id = skill, user_id_id = user, worker_id_id = worker)
        return render(request, "add_project.html",{"skills": skills, "workers":workers})
    

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

def browse(request):
    if request.method == "GET":
        worker = Worker.objects.all()
        skills = Skills.objects.all()
        return render(request, "browse.html",{"worker" : worker,"skills": skills})
    if request.method == "POST":
        city = request.POST["city"]
        skills = request.POST["skill"]
        workers2 = Worker.objects.filter(city = city, skills = skills)
        print(workers2)
        worker = Worker.objects.all()
        skills = Skills.objects.all()
        return render(request, "browse.html", {"workers2":  workers2, "worker" : worker,"skills": skills })
    
def my_profile(request):
    if request.method == "GET":
        if request.session['type'] == "user":
            print(request.session['type'])
            name = request.session['username']
            return render(request, "my_profile.html",{"name": name})
        if request.session['type'] == "worker":
            print(request.session['type'])
            return render(request, "my_profile.html")
        


def my_projects(request):
    if request.method == "GET":
        if request.session['type'] == "user":
            print(request.session['type'])
            name = request.session['username']
            user_id = User.objects.filter(name = name).values_list("id", flat= True).first()
            print(user_id)
            project = Project.objects.all().filter(user_id_id = user_id)
            return render(request, "my_projects.html",{"name": name, "projects": project})
        if request.session['type'] == "worker":
            print(request.session['type'])
            return render(request, "my_projects.html")












