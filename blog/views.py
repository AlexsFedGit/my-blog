from django.shortcuts import render

from blog.models import BlogNote


def index(request):
    notes = BlogNote()[:10]
    context = {
        'notes': notes
    }
    return render(request, 'blog/index.html', context)
