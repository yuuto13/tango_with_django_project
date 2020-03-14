from django.test import TestCase

from django.urls import reverse
from django.utils import timezone

from rango.models import Category, Page


class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        category = Category(name='test', views=-1, likes=0)
        category.save()
        self.assertEqual((category.views >= 0), True)

    def test_slug_line_creation(self):
        category = Category(name='Random Category String')
        category.save()
        self.assertEqual(category.slug, 'random-category-string')

class IndexViewTest(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        add_category('Python', 1, 1)
        add_category('C++', 1, 1)
        add_category('Java', 1, 1)
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python')
        self.assertContains(response, 'C++')
        self.assertContains(response, 'Java')
        self.assertEqual(len(response.context['categories']), 3)

class PageAccessTests(TestCase):
    def test_last_visit_not_in_future(self):
        category = add_category('Django', 1, 1)
        page = add_page(category, 'TwD', 'https://www.tangowithdjango.com')
        
        self.assertTrue(page.last_visit <= timezone.now())
    
    def test_last_visit_is_updated(self):
        category = add_category('Python', 1, 1)
        page = add_page(category, 'Documentation', 'https://docs.python.org/3/')
        created_date = page.last_visit

        response = self.client.get(reverse('rango:goto'), {'page_id': page.id})

        page.refresh_from_db()

        self.assertTrue(page.last_visit > created_date)


# Helper methods
def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()
    return category

def add_page(category, title, url):
    return Page.objects.get_or_create(category=category, title=title, url=url)[0]
