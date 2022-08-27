from django.test import TestCase

from lists.models import Item


class TestItemModel(TestCase):
    def test_saving_and_retrieving_items(self) -> None:
        Item.objects.create(text='The first ever list item')
        Item.objects.create(text='Item the second')

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item, second_saved_item = saved_items
        self.assertEqual(first_saved_item.text, 'The first ever list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
