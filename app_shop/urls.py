from django.urls import path
from . import views

app_name ='app_shop'
urlpatterns = [
    path('', views.index),
    path('/<id>', views.details ),
    path('/buy/<id>', views.update ),
]