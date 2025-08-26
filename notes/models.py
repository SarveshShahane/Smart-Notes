from django.db import models

# Create your models here.


class Note(models.Model):
    title=models.CharField(max_length=100,null=False)
    content=models.TextField(null=False)
    time=models.DateTimeField(auto_now_add=True)
    tags=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.title