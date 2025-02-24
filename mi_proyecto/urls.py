# mi_proyecto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
     path('api/', include('blog.urls')),
    
    # Rutas de inicio de sesión
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # Ruta para la vista index
    path('index/', views.index, name='index'),
]