"""meuImovel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('add',                 views.PropertyCreate.as_view(),        name='property-create'),
    path('<int:pk>',            views.PropertyDetail.as_view(),        name='property-read'),
    path('<int:pk>/update',     views.PropertyUpdate.as_view(),        name='property-update'),
    path('<int:pk>/delete',     views.PropertyDelete.as_view(),        name='property-delete'),
]