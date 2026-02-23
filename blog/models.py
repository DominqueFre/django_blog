from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts', blank=False)
    excerpt = models.TextField(max_length=400, blank=True)
    content = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on'],
        verbose_name = 'Post',
        verbose_name_plural = 'Posts'
