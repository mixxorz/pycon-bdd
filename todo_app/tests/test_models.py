from django.test import TestCase

from ..models import TodoItem


class TodoItemTestCase(TestCase):

    def test_should_save(self):
        item = TodoItem(text='Foo')

        item.save()

        self.assertEqual(TodoItem.objects.first(), item)
