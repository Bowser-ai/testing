from django.test import TestCase
from django.urls import resolve

from lists.models import Item
from lists.views import home_page


class TestHomePage(TestCase):
    def test_root_url_resolves_to_home_page_view(self) -> None:
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self) -> None:
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
