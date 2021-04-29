from django.test import TestCase
from polls.models import Author, Book
from datetime import datetime

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Laura', last_name='Leiner')
    
    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.first_name},{author.last_name}'
        self.assertEqual(expected_object_name, str(author))

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title="Anna Karenina")

    def test_model_str(self):
        book = Book.objects.get(id=1)
        lev = Author.objects.create(first_name="Lev Nyikolajevics", last_name="Tolsztoj")
        self.assertEqual(str(book), "Anna Karenina")
        self.assertEqual(str(lev), "Lev Nyikolajevics,Tolsztoj")


    def test_book_has_an_author(self):
        book = Book.objects.get(id=1)
        lev = Author.objects.create(first_name="Lev Nyikolajevics", last_name="Tolsztoj")
        puskin = Author.objects.create(first_name="Alekszandr Szergejevics", last_name="Puskin")
        lev.book_set.add(book)
        puskin.book_set.add(book)
        self.assertEqual(book.author.count(), 2)
    
    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)
