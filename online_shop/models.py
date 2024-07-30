from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
       class RatingChoices(models.IntegerChoices):

           zero = 0
           one = 1
           two = 2
           three = 3
           four = 4
           five = 5

       name = models.CharField(max_length=100)
       description = models.TextField()
       price = models.DecimalField(max_digits=5, decimal_places=2)
       image = models.ImageField(upload_to='products/',null=True, blank=True)
       category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
       quantity = models.IntegerField(default=1)
       rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
       discount= models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       @property
       def discounted_price(self):
           if self.discount > 0:
               return self.price*(1 - self.discount/100)
           return self.price

       def __str__(self):
           return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=Product.RatingChoices.choices, default=Product.RatingChoices.zero)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.product.name}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    user = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='Pending')

    def save(self, *args, **kwargs):
        self.total_price = self.product.discounted_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order by {self.user} for {self.product.name}'
