# mi_proyecto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    
    #-----rutas inicio sesión
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    #path('', views.PostListView.as_view(), name='posts'),
    path('index/', views.index, name='index'),  # Ruta para la vista index
]