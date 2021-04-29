from django.db import models
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['first_name', 'last_name']
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(to=Author)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    def display_author(self):
        return ', '.join(author.last_name for author in self.genre.all()[:3])

    display_author.short_description = 'Author'

    



