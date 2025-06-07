from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Entry
from .forms import EntryForm 

class EntryListView(ListView):
    model = Entry
    template_name = "mydiary/entry_list.html"
    context_object_name = 'entries'
    
    def get_queryset(self):
        # 新しい日記が上にくるように降順に変更
        return Entry.objects.order_by('-date') 

class EntryDetailView(DetailView):
    model = Entry
    template_name = "mydiary/entry_detail.html" 
    context_object_name = "object"


class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm 
    template_name = "mydiary/entry_form.html"
    success_url = reverse_lazy('mydiary:entry_list') 