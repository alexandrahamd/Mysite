from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductCreateView, ProductDetailView, \
    ProductUpdateWithVersionView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='home'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ProductUpdateWithVersionView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
