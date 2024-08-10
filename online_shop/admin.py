
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Category, Product,Comment,Order
from .Admin_SimpleListFilter import IsVeryExpensiveFilter

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Comment)
# admin.site.register(Order)

admin.site.unregister(Group)
# admin.site.unregister(User)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title','product_count')
    search_fields = ('slug', 'title')
    exclude = ('slug',)
    prepopulated_fields = {'slug':('title',)}
    def product_count(self,obj):
        return obj.products.count()
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'quantity', 'discount','is_very_expensive_product')
    search_fields = ('name', 'price', 'category')
    list_filter = ['category', IsVeryExpensiveFilter]
    exclude = ('slug',)
    prepopulated_fields = {'slug': ('name',)}
    def is_very_expensive_product(self,obj):
        return obj.price > 700
    is_very_expensive_product.boolean = True

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'content')
    search_fields = ('id', 'user', 'product', 'content')
    list_filter = ('user', 'product')
    list_editable = ('content',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'email')
    search_fields = ('id', 'user', 'product', 'email')
    list_filter = ('user', 'product')



