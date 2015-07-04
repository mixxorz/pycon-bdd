from behave import given, when, then

from todo_app.models import TodoItem


@then(u'I should see "{text}"')
def should_see(context, text):
    context.test.assertTrue(context.browser.is_text_present(text),
                            '"%s" was not found' % text)


@given(u'there are no todo items')
def no_todo_items(context):
    context.test.assertEqual(0, TodoItem.objects.count())


@given(u'there is one todo item')
def one_todo_items(context):
    TodoItem.objects.create(text='First todo item')
    context.browser.reload()


@when(u'I add "{text}"')
def add_todo_item(context, text):
    context.browser.fill('todo_item', text)
    context.browser.find_by_id('btnSubmit').first.click()


@given(u'the following todo items')
def table_todo_items(context):
    for row in context.table:
        TodoItem.objects.create(text=row['todo_items'])

    context.browser.reload()


@when(u'I delete "{text}"')
def delete_todo_item(context, text):
    context.browser.find_by_css('[data-text="%s"]' % text).first.click()


@then(u'I should not see "{text}"')
def step_impl(context, text):
    context.test.assertFalse(context.browser.is_text_present(text),
                             '"%s" was found' % text)
