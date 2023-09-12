from django.urls import path
from qr import views
urlpatterns = [
    path('', views.index),
    path('scan/', views.scan_view, name='scan'),
]