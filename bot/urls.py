from django.urls import path
from .views import GetList,NumberBut
urlpatterns = [
    path('button',GetList.as_view(),name='button-list'),
    path('number',NumberBut.as_view(),name='number')
]