from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('create/', create_task, name='create_task'),
    path('delete/<int:pk>', delete_task, name='delete_task'),
    path('update/<int:pk>', update_task, name='update_task'),
    path('login/', login_view, name='login_url'),
    path('signup/', sign_up, name='sign-up')
]
