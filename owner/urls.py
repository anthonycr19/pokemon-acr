from django.urls import path
from . import views

urlpatterns = [
    path('owner_list/', views.owner_list, name='owner_list'),
    path('owner_orm/', views.owner_orm, name='owner_orm'),
    path('owner_search/', views.owner_search, name='owner_search')
]

