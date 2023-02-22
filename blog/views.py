from string import punctuation, whitespace

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from blog.forms import NoteForm
from blog.models import BlogNote


class IndexView(View):
    """Main page of blog"""
    def get(self, request):
        if request.user is None:
            notes = BlogNote.objects.filter(is_published=True)[:10]
        else:
            notes = BlogNote.objects.all()[:10]
        for note in notes:
            note.body = self.slice_text(note.body, max_length=240, str_at_end='... [читать далее]')
        context = {
            'notes': notes
        }
        return render(request, 'blog/index.html', context)

    @staticmethod
    def slice_text(text, max_length=240, str_at_end=''):
        if len(text) < max_length:
            return text
        while text[max_length] not in punctuation and text[max_length] not in whitespace:
            max_length -= 1
        return text[:max_length] + str_at_end


class NoteDetailView(View):
    """Get detail view of blog's note"""
    def get(self, request, note_id):
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
        return render(request, 'blog/note_create.html', context)

    def post(self, request, *args, **kwargs):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'blog/note_create.html')


class NoteUpdateView(View):
    """Update exiting note"""
    def get(self, request, note_id):
        note = get_object_or_404(BlogNote, pk=note_id)
        form = NoteForm(instance=note)
        note_next = BlogNote.objects.filter(pk__gt=note_id).last()
        note_prev = BlogNote.objects.filter(pk__lt=note_id).first()
        context = {
            'note': note,
            'form': form,
            'note_next': note_next,
            'note_prev': note_prev,
        }
        return render(request, 'blog/note_update.html', context)

    def post(self, request, note_id, *args, **kwargs):
        note = get_object_or_404(BlogNote, pk=note_id)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('blog:detail', kwargs={'note_id': note_id}))
        context = {
            'form': form,
            'note_id': note_id,
        }
        return render(request, 'blog/note_update.html', context)


class NoteDelete(View):
    """Remove single note from blog"""
    def get(self, request, note_id):
        note = get_object_or_404(BlogNote, pk=note_id)
        context = {
            'note': note,
        }
        return render(request, 'blog/note_delete.html', context)

    def post(self, request, note_id, *args, **kwargs):
        note = get_object_or_404(BlogNote, pk=note_id)
        note.delete()
        note_prev = BlogNote.objects.filter(pk__lt=note_id).first()
        if note_prev:
            return redirect(reverse_lazy('blog:update', kwargs={'note_id': note_prev.id}))
        return redirect(reverse_lazy('blog:index'))