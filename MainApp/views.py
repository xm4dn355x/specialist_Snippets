from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .models import Snippet

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов',
               'snippets': snippets}
    return render(request, 'pages/view_snippets.html', context)


def snippets_details(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    context = {'pagename': snippet.name,
               'snippet': snippet}
    return render(request, 'pages/snippet_details.html', context)


# @csrf_protect()
def form_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        lang = request.POST['lang']
        code = request.POST['code']
        snippet = Snippet(name=name, lang=lang, code=code)
        snippet.save()
        print(f"{request.POST}")
        return redirect('snippets_list')