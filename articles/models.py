from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True, upload_to='article_pics')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body) > 400:
            return self.body[:400] + '...'
        else:
            return self.body

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})