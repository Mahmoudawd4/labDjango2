from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    # title = models.CharField(max_length=40)
    # # body = models.TextField(max_length=200)
    # is_completed = models.BooleanField(default=False)
    # # description  = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=date.today())
    title = models.CharField(max_length=40)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    # def getBody(self):
    #     return self.body[:50] +'...'
    # def __str__(self):
    #     return f'{self.title}: {self.body[:50] +"..."}'

    def __str__(self):
            return self.title
        
class TodoItem(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    todo = models.ForeignKey(Todo, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    
    def getBody(self):
        return self.body[:100]+'...'