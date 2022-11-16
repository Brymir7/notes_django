from django.urls import path
from .views import NoteDetail, NoteDelete, NoteCreate, NoteUpdate, DayUpdate, DayDetail
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('note-detail/<int:note_id>/', NoteDetail.as_view(), name = 'note-detail'),
    path('note-create/', NoteCreate.as_view(), name = 'note-create'),
    path('note-delete/<str:pk>/', NoteDelete.as_view(), name = 'note-delete'),
    path('note-update/<int:pk>/', NoteUpdate.as_view(), name = 'note-update'),
    path('day-update/<int:pk>', DayUpdate.as_view(), name = 'day-update'),
    path('day-detail/<int:day_id>/', DayDetail.as_view(), name = 'day-detail'),
]