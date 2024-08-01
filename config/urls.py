from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from online_shop import views
from config import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
    path('categories/<int:category_id>/', views.index, name='category_detail'),
    path('', views.index, name='index'),
    path('detail/<int:product_id>/add_comment/', views.add_comment, name='add_comment'),
    path('order/add/<int:product_id>/', views.add_order, name='add_order'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
