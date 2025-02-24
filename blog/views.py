from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post

from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

def hola_mundo(request):
    return HttpResponse("Hola Mundo")


'''def index(request):
    contexto = {
        'titulo': 'Bienvenidos a mi Blog',
        'contenido': 'Este es el primer post de mi blog.',
    }
    return render(request, 'index.html', contexto)
'''
def index(request):
    # Obtener todos los posts de la base de datos
    posts = Post.objects.all()
    # Pasar los posts a la plantilla index.html
    return render(request, 'index.html', {'posts': posts})
    
class PostListView(ListView):
    model = Post
    template_name = '/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('post-list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('post-list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')