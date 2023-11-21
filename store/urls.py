from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_season,
    modificar,
    eliminar,
    SupplierListView,
    BuyerListView,
    SeasonListView,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-season/', create_season, name='create-season'),
    path('modificar/', modificar, name='modificar'),
    path('eliminar/', eliminar, name='eliminar'),
    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),

]
