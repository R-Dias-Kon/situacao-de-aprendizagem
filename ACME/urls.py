"""
URL configuration for ACME project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from ACMEAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.visao_geral, name='visao-geral'),
    path('create/', views.tarefa_adicionar, name='adicionar-tarefa'),
    path('all/', views.tarefa_consultar, name='consultar-tarefas'),
    path('update/<int:pk>/', views.tarefa_atualizar, name='atualizar-tarefa'),
    path('tarefa/<int:pk>/delete', views.tarefa_deletar, name='deletar-tarefa'),
]
