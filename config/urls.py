from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from online_shop import views
from config import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
