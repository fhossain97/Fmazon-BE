from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('', views.home, name='home'),
    path('items/', views.ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail')
]