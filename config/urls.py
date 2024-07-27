
from django.contrib import admin
from django.urls import path
from online_shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detail.html/',views.product_detail,name='detail'),
]
