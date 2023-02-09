from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    city = models.CharField(max_length=256)

    def __str__(self) -> str:
        return super().__str__()
    
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=256)
    skill_description = models.TextField(default="")
    workers = models.ManyToManyField(Worker)
    

    def __str__(self) -> str:
        return super().__str__()