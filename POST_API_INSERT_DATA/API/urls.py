from django.urls import path
from . import views

urlpatterns = [
    path('insert-data/',views.API_Insert_Data,name='insert-data'),
]
