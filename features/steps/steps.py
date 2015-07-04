from behave import given, when, then

from todo_app.models import TodoItem


@then(u'I should see "{text}"')
def should_see(context, text):
    context.test.assertTrue(context.browser.is_text_present(text),
                            '"%s" was not found' % text)


@given(u'there are no todo items')
def no_todo_items(context):
    context.test.assertEqual(0, TodoItem.objects.count())


@when(u'I add "{text}"')
def buy_pycon_tickets(context, text):
    context.browser.fill('todo_item', text)
    context.browser.find_by_id('btnSubmit').first.click()
