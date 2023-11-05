from django.urls import path
from .views import ComputerList, ComputerCreate, ComputerDelete


urlpatterns = [
    path('', ComputerList.as_view(), name='mainpage'),
    path('create/', ComputerCreate.as_view(), name='create'),
    path('delete/<int:computer_id>', ComputerDelete.as_view(), name='delete')
]