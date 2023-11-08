from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):


    created_by = models.ForeignKey(User, related_name='lead', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return (f"{self.name}")