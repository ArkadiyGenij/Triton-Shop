from django.urls import path

from shop import views
from shop.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, ProductDeleteView

app_name = 'shop'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/products', ProductListView.as_view(), name='admin-products'),
    path('dashboard/products/create', ProductCreateView.as_view(), name='admin-products-create'),
    path('dashboard/products/edit/<int:pk>', ProductUpdateView.as_view(), name='admin-products-update'),
    path('dashboard/products/detail/<int:pk>', ProductDetailView.as_view(), name='admin-products-detail'),
    path('dashboard/products/delete/<int:pk>', ProductDeleteView.as_view(), name='admin-products-delete'),
]
