from django.urls import path
from .views import home, update_task, delete_task

urlpatterns = [
    path('', home, name='home'),
    path('edit/<str:pk>', update_task, name='edit'),
    path('delete/<str:pk>', delete_task, name='delete')
]
