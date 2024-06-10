from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:id>', views.Edit, name='edit'),
    path('delete/<int:id>', views.Delete, name='delete')
]