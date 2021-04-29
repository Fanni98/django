from django.shortcuts import render
from .models import Author, Book
from django.views import generic

def index(request):
    
    num_books = Book.objects.all().count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    
class AuthorListView(generic.ListView):
    model = Author
    
class BookDetailView(generic.DetailView):
    model = Book
    
class AuthorDetailView(generic.DetailView):
    model = Author
    