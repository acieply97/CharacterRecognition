from django.db import models
import os


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    choice = models.CharField(max_length=1, choices=(('p', 'pdf'), ('t', 'txt')), default='p')

    def filename(self):
        return os.path.basename(self.document.name)

