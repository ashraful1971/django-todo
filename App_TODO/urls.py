from django.urls import path
from . import views

app_name = 'App_TODO'

urlpatterns = [
    path('', views.index, name='index'),
    path('/add', views.addItem, name='add'),
    path('/delete/<pk>', views.removeItem, name='delete'),
    path('/edit/<pk>', views.editItem, name='edit'),
    path('/update', views.updateItem, name='update'),
]