from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('detail/<str:slug>/', BlogDetailView.as_view(), name='detail'),
    path('update/<str:slug>/', BlogUpdateView.as_view(), name='update')
]
