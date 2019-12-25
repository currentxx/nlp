"""WebApiProjesi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ApiProje import views
urlpatterns = [
    path('',views.index,name="index"),
    path('api/kurlar/<int:idler>/', views.KurListesiGetirIdyeGore.as_view(),name="KurListesiGetirIdyeGore"),
    path('api/kurlar/<str:isim>/', views.KurListesiGetirDovizeGore.as_view(), name="KurListesiGetirDovizeGore"),
    path('api/kurlar/',views.index,name="index"),
    path('api/kurlar/Ekle/Yeni', views.KurListesiCreate.as_view(), name="KurListesiCreate"),
    path('api/kurlar/detay/<int:pk>/',views.KurDetaylari,name="KurDetaylariGetir"),
    path('api/ozet/getir/', views.OzetGetir.as_view(), name="OzetGetir"),
    path('api/ozet/ekle/', views.OzetCreate.as_view(), name="OzetCreate"),
]
