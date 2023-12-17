from django.urls import path
from . import views

urlpatterns = [
    path('owner_list/', views.owner_list, name='owner_list'),
    path('owner_orm/', views.owner_orm, name='owner_orm'),
    #path('owner_detail/<int:id_owner>', views.owner_detail, name="owner_edit"),
]

