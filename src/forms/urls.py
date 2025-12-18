from django.contrib import admin
from django.urls import path, include
from . import views 

app_name = 'forms'

urlpatterns = [
    path('', views.createMessage_view, name="Home"),
    path('admin/', views.getAllMessages_view, name="mensagens"),
    path('delete/<int:id>', views.deleteMessageById_view, name="deletar"),
    path('edit/<int:id>', views.editMessageById_view, name="editar"),
]