from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('add/', add_musician, name='add_musician'),
    path('edit/<int:id>', edit_musician, name='edit_musician'),
    path('delete/<int:id>', delete_musician, name='delete_musician'),
]
