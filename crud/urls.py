from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('create/', create_task, name='create_task'),
    path('delete/<int:pk>', delete_task, name='delete_task'),
    path('update/<int:pk>', update_task, name='update_task'),
]
