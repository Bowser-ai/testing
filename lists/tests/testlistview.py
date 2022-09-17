from django.test import TestCase

from lists.models import Item, List


class TestListView(TestCase):
    def test_display_all_items(self) -> None:
        list_ = List.objects.create()
        item_1 = Item.objects.create(text='item_1', list=list_)
        item_2 = Item.objects.create(text='item_2', list=list_)

        response = self.client.get(f'/lists/{list_.id}/')
        self.assertContains(response, item_1.text)
        self.assertContains(response, item_2.text)

    def test_view_invokes_correct_template(self) -> None:
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_can_save_a_POST_request(self) -> None:
        self.client.post('/lists/new/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_a_POST(self) -> None:
        response = self.client.post(
            '/lists/new/',
            data={'item_text': 'A new list item'}
        )
        list_ = List.objects.first()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/lists/{list_.id}/')

    def test_correct_list_passed_to_template(self) -> None:
        correct_list = List.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)
