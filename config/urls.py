from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from online_shop.views import views
from config import settings
from online_shop.views import auth
urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<slug:product_slug>/', views.product_detail, name='detail'),
    path('categories/<slug:category_slug>/', views.index, name='category_detail'),
    path('', views.index, name='index'),
    path('detail/<slug:product_slug>/add_comment/', views.add_comment, name='add_comment'),
    path('detail/<slug:product_slug>/add_order', views.add_order, name='add_order'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<slug:product_slug>/', views.delete_product, name='delete_product'),
    path('edit_product/<slug:product_slug>/', views.edit_product, name='edit_product'),
    # login,register
    path('login_page/', auth.login_page, name='login_page'),
    path('register_page/', auth.register_page, name='register_page'),
    path('logout_page/',auth.logout_page, name='logout_page')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

