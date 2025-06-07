from django.urls import path
from .views import EntryListView, EntryDetailView, EntryCreateView

app_name = "mydiary"

urlpatterns = [
    path("entry_list/", EntryListView.as_view(), name="entry_list"),
    path("entry_detail/<int:pk>/", EntryDetailView.as_view(), name="entry_detail"),
    path("entry_create/", EntryCreateView.as_view(), name="entry_create"), 
]