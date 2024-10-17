from django.conf import settings
from django.db import models # essa linha era a única que já vem no arquivo.
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)
    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()
    def __str__(self):
        return self.title