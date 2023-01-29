from django.shortcuts import render, get_object_or_404

from blog.models import BlogNote


def index(request):
    notes = BlogNote.objects.filter(hidden=False)[:10]
    for note in notes:
        if len(note.body) > 240:
            note.body = note.body[:237] + "..."
    context = {
        'notes': notes
    }
    return render(request, 'blog/index.html', context)


def note_detail(request, note_id):
    note = get_object_or_404(BlogNote, pk=note_id)
    note_next = BlogNote.objects.filter(pk__gt=note_id).last()
    note_prev = BlogNote.objects.filter(pk__lt=note_id).first()
    context = {
        'note': note,
        'note_next': note_next,
        'note_prev': note_prev,
    }
    return render(request, 'blog/note_detail.html', context)
