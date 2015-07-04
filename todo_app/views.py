from django.views.generic import TemplateView


class TodoView(TemplateView):
    template_name = 'todo_list.html'

todo_view = TodoView.as_view()
