from django.urls import path
from . import views
urlpatterns = [
    path('', views.figma_copy, name='figma_copy'),
]