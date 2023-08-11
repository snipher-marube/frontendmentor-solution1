from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('addons/', views.addons, name='addons'),
    path('summary/', views.summary, name='summary'),
    path('success/', views.success, name='success'),
]