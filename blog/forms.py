from django.forms import ModelForm

from blog.models import BlogNote


class NoteForm(ModelForm):
    """Basic form for create,update note from blog"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
    class Meta:
        model = BlogNote
        fields = ('body', 'is_published')
