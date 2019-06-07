"""Django_DnD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from django.urls.conf import re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('', views.inicio),
    path('crearPersonaje/', views.newCharacter),
    path('seleccionarSubclase/<int:character_id>', views.selectSubclass),
    path('seleccionarHechizos/<int:character_id>', views.selecSpells),
    path('personajeSeleccionado/<int:character_id>', views.personajeSeleccionado),
    path('mostrarHechizos/', views.mostrarHechizos),
    path('searchSpell/',views.searchSpell),
    path('personajeSeleccionado/', views.personajeSeleccionado),
    path('modificarStats/<int:character_id>', views.modificarStats),
    path('personajeSeleccionado/', views.personajeSeleccionado),
    path('seleccionarHechizos/', views.seleccionarHechizos),
    path('recomendarHechizos/', views.recomendarHechizos),
    path('login/',auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html')),
    re_path(r'^auth/',include(urls)),
    path('signup/', views.SignUp.as_view(success_url="/login"), name='signup'),
#     path('ajax/load-subclass/', views.load_subclass, name='ajax_load_subclass')
]
