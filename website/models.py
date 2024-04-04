from django.db import models

class Contact(models.Model):
    
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)
    
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.email