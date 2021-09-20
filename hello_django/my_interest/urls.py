from django.urls import path
from . import views
urlpatterns = [
    path('', views.interest_page, name='interest_page'),
]