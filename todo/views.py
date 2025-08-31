from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView
from django.views.generic.detail import SingleObjectMixin

from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    paginate_by = None

    def get_queryset(self):
        return Task.objects.select_related().prefetch_related('tags').order_by('is_done', '-created_at')


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:home')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:home')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:home')


class ToggleTaskStatusView(SingleObjectMixin, RedirectView):
    model = Task
    url = reverse_lazy('todo:home')

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.is_done = not obj.is_done
        obj.save(update_fields=['is_done'])
        return HttpResponseRedirect(self.url)


class TagListView(generic.ListView):
    model = Tag
    template_name = 'todo/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('todo:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('todo:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'todo/tag_confirm_delete.html'
    success_url = reverse_lazy('todo:tag-list')
