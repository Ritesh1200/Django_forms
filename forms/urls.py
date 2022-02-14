from django.urls import path 
from .views import NormalForm , ModalForm

urlpatterns = [
    path('normal', NormalForm , name = "normalform"),
    path('model', ModalForm , name = "modalform")
]