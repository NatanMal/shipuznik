from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    password =  models.CharField( max_length=256, default="")

    def __str__(self) -> str:
        return super().__str__()
    
class User(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    password =  models.CharField( max_length=256, default="")

    def __str__(self) -> str:
        return super().__str__()
    

    
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=256)
    skill_description = models.TextField(default="")
    workers = models.ManyToManyField(Worker)
    

    def __str__(self) -> str:
        return super().__str__()
    
class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skills,on_delete=models.CASCADE)
    worker_id =  models.ForeignKey(Worker,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()