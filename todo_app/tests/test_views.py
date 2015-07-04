from django.core.urlresolvers import reverse
from django.test import TestCase


class TodoViewTestCase(TestCase):

    def test_should_return_view(self):
        response = self.client.get(reverse('todo_view'))

        self.assertEqual(200, response.status_code)
