from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.note_detail, name='detail'),
    path('new/', views.NoteAdd.as_view(), name='create'),
]
