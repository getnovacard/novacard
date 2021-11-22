from django.db import models

class Template(models.Model):
    template_name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    template_path = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.template_name 
