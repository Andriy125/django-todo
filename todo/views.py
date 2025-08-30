from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

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


def toggle_task_status(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save(update_fields=['is_done'])
    return redirect('todo:home')


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
