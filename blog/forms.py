from django.forms import ModelForm

from blog.models import BlogNote


class NoteForm(ModelForm):
    """Basic form for create,update note from blog"""
    class Meta:
        model = BlogNote
        fields = ('body', 'is_published')
