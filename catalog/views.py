from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre, Language

# Create your views here.


def index(request):
    context = {
        'num_books': Book.objects.count(),
        'num_instances': BookInstance.objects.count(),
        'num_available_instances': BookInstance.objects.filter(status='a').count(),
        'num_authors': Author.objects.count(),
    }

    return render(
        request,
        'index.html',
        context=context
    )
