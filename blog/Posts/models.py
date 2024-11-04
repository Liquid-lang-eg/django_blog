from django.db import models
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Posts:post_detail', args=[str(self.id)])


