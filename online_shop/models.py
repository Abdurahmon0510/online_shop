from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     class Meta:
         abstract = True
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
           self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'category'

class Product(BaseModel):
       class RatingChoices(models.IntegerChoices):

           zero = 0
           one = 1
           two = 2
           three = 3
           four = 4
           five = 5

       name = models.CharField(max_length=100)
       description = models.TextField()
       price = models.FloatField()
       image = models.ImageField(upload_to='products/', null=True, blank=True)
       category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
       quantity = models.IntegerField(default=1)
       rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
       discount = models.FloatField( null=True, blank=True)
       slug = models.SlugField(unique=True, null=True, blank=True)
       class Meta:
           db_table = 'products'

       @property
       def discounted_price(self):
           if self.discount > 0:
              return self.price*(1 - self.discount/100)
           return self.price

       def __str__(self):
           return self.name

class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_provide = models.BooleanField(default=True)
    class Meta:
        db_table = 'comments'

    def __str__(self):
        return f'Comment by {self.user} on {self.product.name}'


class Order(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    user = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    email = models.EmailField(blank=True, null=True)
    class Meta:
        db_table = 'orders'


    def __str__(self):
        return f'Order by {self.user} for {self.product.name}'
