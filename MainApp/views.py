from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .models import Snippet
from .forms import SnippetForm

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            raise PermissionDenied
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('index')


def add_snippet_page(request):
    form = SnippetForm()
    context = {'pagename': 'Добавление нового сниппета', 'form': form}
    if request.method == 'GET':
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets_list')
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