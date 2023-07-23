from django.urls import path 
from .views import * 
urlpatterns = [
    path('loginpage', login_page , name='login_page'),
    path('logoutpage', logout_page , name='logout_page'),
    path('register_user', register_user , name='register_user')
]
