from django.urls import path 
from .views import *


urlpatterns = [
    path('', homepage , name='homepage'),
    path('question/<str:pk>', view_question , name='view_question'),
    path('react/<str:pk>/<str:type>', question_react , name='react')
]