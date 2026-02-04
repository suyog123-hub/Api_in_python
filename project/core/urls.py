from django.urls import path
from .views import *
urlpatterns = [
    path('test/',APITestView.as_view(),name='test'),
    path('test/<id>',APITestView.as_view()),
]
