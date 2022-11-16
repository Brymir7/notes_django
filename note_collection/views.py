from audioop import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Note, Month, Day
def index(request):
    note_collection = Note.objects.order_by('-pub_date')
    months = Month.objects.all()
    return render(request, 'note_collection/index.html', {'note_collection' : note_collection, 'months': months})

class NoteCreate(CreateView):
    model = Note
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('index')
class NoteDetail(DetailView):
    model = Note
class NoteDelete(DeleteView):
    model = Note
class NoteUpdate(UpdateView):
    model = Note
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('index')
class DayDetail(DetailView):
    model = Day
class DayUpdate(UpdateView):
    model = Day
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('index')
# Create your views here.
