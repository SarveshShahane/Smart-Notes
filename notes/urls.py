from django.urls import path

from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('create/', views.create_note, name='create_note'),
    path('search/', views.search_notes, name='search_notes'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]