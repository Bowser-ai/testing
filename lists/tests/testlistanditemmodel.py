from django.test import TestCase

from lists.models import Item, List


class TestListAndItemModel(TestCase):
    def test_saving_and_retrieving_items(self) -> None:
        list_ = List.objects.create()
        Item.objects.create(text='The first ever list item', list=list_)
        Item.objects.create(text='Item the second', list=list_)

        saved_list = List.objects.first()
        self.assertEqual(list_, saved_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item, second_saved_item = saved_items
        self.assertEqual(first_saved_item.text, 'The first ever list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.list, list_)

    def test_can_save_new_items_to_existing_list(self) -> None:
        List.objects.create()
        correct_list = List.objects.create()
        self.client.post(
            f'/lists/{correct_list.id}/add-item/',
            data={'item_text': 'item_1'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'item_1')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_correct_list(self) -> None:
        List.objects.create()
        correct_list = List.objects.create()
        response = self.client.post(
            f'/lists/{correct_list.id}/add-item/',
            data={'item_text': 'item_1'}
        )
        self.assertRedirects(response, f'/lists/{correct_list.id}/')
