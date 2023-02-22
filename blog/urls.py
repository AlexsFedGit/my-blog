from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.NoteAdd.as_view(), name='create'),
    path('<int:note_id>/', views.NoteDetailView.as_view(), name='detail'),
    path('edit/<int:note_id>/', views.NoteUpdateView.as_view(), name='update'),
    path('delete/<int:note_id>/', views.NoteDelete.as_view(), name='delete'),
]
