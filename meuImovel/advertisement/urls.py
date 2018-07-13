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
    path('add',                 views.AdvertisementCreate.as_view(),        name='advertisement-create'),
    path('<int:pk>',            views.AdvertisementDetail.as_view(),        name='advertisement-read'),
    path('<int:pk>/update',     views.AdvertisementUpdate.as_view(),        name='advertisement-update'),
    path('<int:pk>/delete',     views.AdvertisementDelete.as_view(),        name='advertisement-delete'),
    path('list',                views.AdvertisementList.as_view(),          name='advertisement-list'),
    path('',                    views.AdvertisementList.as_view(),          name='advertisement-list'),
]
