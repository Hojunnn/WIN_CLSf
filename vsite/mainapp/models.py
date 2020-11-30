from django.db import models

# Create your models here.
class UploadDocument(models.Model):
    docfile = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'upload_document'

