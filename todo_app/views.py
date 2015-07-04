from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import ListView

from .models import TodoItem


class TodoView(ListView):
    context_object_name = 'todo_items'
    model = TodoItem
    template_name = 'todo_list.html'

    def post(self, request, *args, **kwargs):
        TodoItem.objects.create(text=request.POST['todo_item'])
        return redirect(reverse('todo_view'))

todo_view = TodoView.as_view()
