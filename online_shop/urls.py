from django.urls import path
from online_shop import views
urlpatterns = [
    path('detail.html/', views.product_detail, name='detail.html'),
]
