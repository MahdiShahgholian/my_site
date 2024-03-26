from django.db import models

class Content(models.Model):
    
    name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
