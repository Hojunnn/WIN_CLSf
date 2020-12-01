from django.db import models

# Create your models here.
class UploadDocument(models.Model):
    docfile = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    exe_name = models.CharField(max_length=100, blank=True, null=True)
    ico = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_document'


