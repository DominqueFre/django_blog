from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class About(models.Model):

    developer = models.CharField(max_length=100, unique=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='about_info', blank=False)
    content = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.developer} | written by {self.author}"

    class Meta:
        verbose_name = 'About the Developer'
        verbose_name_plural = 'About the Developers'
