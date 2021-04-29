from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from catalog.models import Author, BookInstance, Book, Genre
import datetime

# Create your tests here.

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_authors = 13

        for author_id in range(number_of_authors):
            Author.objects.create(
                first_name=f'Magda {author_id}',
                last_name=f'Szabó {author_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 10)

    def test_lists_all_authors(self):
        response = self.client.get(reverse('authors')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 3)


class LoanedBookInstancesByUserListViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='molylepke', password='szeretemakönyveket12')
        test_user2 = User.objects.create_user(username='user2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        test_author = Author.objects.create(first_name='J. K.', last_name='Rowling')
        test_genre = Genre.objects.create(name='Fikció')
        test_book = Book.objects.create(
            title='Legendás állatok és megfigyelésük',
            summary='Rövid összefoglaló',
            isbn='9781408896945',
            author=test_author,
        )

        genre_objects_for_book = Genre.objects.all()
        test_book.genre.set(genre_objects_for_book)
        test_book.save()

        number_of_book_copies = 30
        for book_copy in range(number_of_book_copies):
            return_date = timezone.localtime() + datetime.timedelta(days=book_copy%5)
            the_borrower = test_user1 if book_copy % 2 else test_user2
            status = 'm'
            BookInstance.objects.create(
                book=test_book,
                imprint='Unlikely Imprint, 2016',
                due_back=return_date,
                borrower=the_borrower,
                status=status,
            )

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='molylepke', password='szeretemakönyveket12')
        response = self.client.get(reverse('my-borrowed'))

        self.assertEqual(str(response.context['user']), 'molylepke')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'catalog/bookinstance_list_borrowed_user.html')