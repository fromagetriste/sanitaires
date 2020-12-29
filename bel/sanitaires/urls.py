from django.urls import path
from . import views

urlpatterns = [
    path('sanitaires/', views.sanitaires, name='sanitaires'),
    path('sanitaires/success/', views.success, name='success'),
    path('sanitaires/fonctiondate/', views.sanitaires, name='fonctiondate'),
]
