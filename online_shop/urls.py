from django.urls import path
from online_shop import views
urlpatterns = [

    path('categories/', views.product_detail, name='categories'),




]
