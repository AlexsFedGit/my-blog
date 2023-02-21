from string import punctuation, whitespace

from django.shortcuts import render, get_object_or_404
from django.views import View

from blog.forms import NoteForm
from blog.models import BlogNote

def slice_text(text, max_length=240, str_at_end=''):
    if len(text) < max_length:
        return text
    while text[max_length] not in punctuation and text[max_length] not in whitespace:
        max_length -= 1
    return text[:max_length] + str_at_end


def index(request):
    if request.user is None:
        notes = BlogNote.objects.filter(is_published=True)[:10]
    else:
        notes = BlogNote.objects.all()[:10]
    for note in notes:
        note.body = slice_text(note.body, max_length=240, str_at_end='... [читать далее]')
    context = {
        'notes': notes
    }
    return render(request, 'blog/index.html', context)


def note_detail(request, note_id):
    """Get detail view of blog's note"""
    note = get_object_or_404(BlogNote, pk=note_id)
    note_next = BlogNote.objects.filter(pk__gt=note_id).last()
    note_prev = BlogNote.objects.filter(pk__lt=note_id).first()
    context = {
        'note': note,
        'note_next': note_next,
        'note_prev': note_prev,
    }
    return render(request, 'blog/note_detail.html', context)


class NoteAdd(View):
    """Give access for creating new notes"""
    def get(self, request, *args, **kwargs):
        form = NoteForm()
        context = {
            'form': form
        }
        return render(request, 'blog/note_add.html', context)

    def post(self, request, *args, **kwargs):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'blog/note_add.html')
