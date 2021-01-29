from django.db import models

# Create your models here.

class Document(models.Model):
    doc_file = models.FileField(upload_to='products_page')
