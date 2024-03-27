from django.db import models

class Post(models.Model):
    #image
    #auther
    title = models.CharField(max_length=20)
    content = models.TextField()
    #tag
    #category
    counted_view = models.IntegerField(default= 0)
    status = models.IntegerField(default= True)
    publish_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)
    
    def __str__(self):
        return self.title