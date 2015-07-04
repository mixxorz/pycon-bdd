from splinter import Browser


def before_scenario(context, scenario):
    context.browser = Browser('firefox')
    context.browser.visit(context.get_url('todo_view'))


def after_scenario(context, scenario):
    context.browser.quit()
    del context.browser
