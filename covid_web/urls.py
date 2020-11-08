from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('register/', views.detail, name='register'),
    path('country/', views.details, name='details')
]