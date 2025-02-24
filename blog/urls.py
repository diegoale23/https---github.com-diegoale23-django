# blog/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('hola/', views.hola_mundo, name='hola_mundo'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('index/', views.index, name='index'),  # Ruta para la vista index en el blog
    path('posts/', PostListView.as_view(), name='post-list'),
    path('nuevo/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/eliminar/', PostDeleteView.as_view(), name='post-delete'),
    
    # Rutas para la API
    path('api/posts/', PostListAPIView.as_view(), name='api-post-list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-post-detail'),
]