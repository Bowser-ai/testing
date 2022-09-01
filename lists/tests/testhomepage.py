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

    def test_can_save_a_POST_request(self) -> None:
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_a_POST(self) -> None:
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/only-list-in-the-world')

    def test_only_save_items_when_necessary(self) -> None:
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
