# blog/urls.py
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('hola/', views.hola_mundo, name='hola_mundo'),
    path('', views.index, name='index'),  # Ruta para la vista index en el blog
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('nuevo/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/editar/', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/eliminar/', views.PostDeleteView.as_view(), name='post-delete'),
]