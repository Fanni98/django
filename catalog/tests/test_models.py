from django.test import TestCase
from catalog.models import Author, Book, Genre
# Create your tests here.

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Laura', last_name='Leiner')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='Szent Johanna Gimi')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)
    
    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEqual(max_length, 200)
    
    def test_book_has_a_genre(self):
        book = Book.objects.get(id=1)
        genre1=Genre.objects.create(name='romantikus')
        genre2=Genre.objects.create(name='iskolai')
        book.genre.set([genre1.pk, genre2.pk])
        self.assertEqual(book.genre.count(), 1)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')