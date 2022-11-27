from django.urls import path
from . import views

urlpatterns = [
    # define a route for home
    path('home/', views.home, name='home'),
    path('webhook/', views.webhook, name='webhook'),
]
