from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=100,unique=True)

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
       discount= models.DecimalField(max_digits=5,decimal_places=2,default=0)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       @property
       def discounted_price(self):
           if self.discount > 0:
               return self.price*( 1 - self.discount/100)
           return self.price

       def __str__(self):
           return self.name






# Create your models here.
