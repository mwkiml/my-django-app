from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
    path('about/', about),  # about URL 추가
]
