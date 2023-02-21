from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:note_id>/', views.NoteDetailView.as_view(), name='detail'),
    path('new/', views.NoteAdd.as_view(), name='create'),
]
