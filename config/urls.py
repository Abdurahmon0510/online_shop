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
    path('detail/<int:product_id>/add_order', views.add_order, name='add_order'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/',views.delete_product, name='delete_product'),
    path('edit_product/<int:product_id>/',views.edit_product, name='edit_product'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
