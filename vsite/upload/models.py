from django.db import models

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/' )
    name = models.CharField(max_length=100,default="",null=True)
    exe_name = models.CharField(max_length=100,default="",null=True)
    category = models.CharField(max_length=100,default="",null=True)
    ico = models.CharField(max_length=100,default="",null=True)
    def __str__(self):
        return self.name
