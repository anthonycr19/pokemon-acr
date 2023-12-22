from django.urls import path
from . import views

urlpatterns = [
    path('owner_list/', views.owner_list, name='owner_list'),
    path('owner_orm/', views.owner_orm, name='owner_orm'),
    path('owner_search/', views.owner_search, name='owner_search'),

    path('owner_details/', views.owner_details, name='owner_details'),
    path('owner_delete/<int:id_owner>', views.owner_delete, name='owner_delete'),
    path('owner_edit/<int:id_owner>', views.owner_edit, name='owner_edit'),
    path('owner_create/', views.owner_create, name='owner_create'),

    #URLs para las VBC
    path('owner_list_vc/', views.OwnerList.as_view(), name="owner_list_vc"),
    path('owner_create_vc/', views.OwnerCreate.as_view(), name="owner_create_vc"),
    path('owner_edit_vc/<int:pk>', views.OwnerUpdate.as_view(), name="owner_edit_vc"),
    path('owner_delete_vc/<int:pk>', views.OwnerDelete.as_view(), name="owner_delete_vc"),

    #URLs DRF
    path('owner_list_drf_def/', views.owner_api_view, name="owner_list_drf_def"),
    path('owner_detail_drf_def/<int:pk>', views.owner_details_view, name="owner_detail_drf_def")

]

