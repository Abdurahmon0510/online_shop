from django.forms import ModelForm,forms
from online_shop.models import Comment, Order, Product


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        exclude =('product',)

    def clean_email(self):
       email=self.cleaned_data.get('email')
       if Comment.objects.filter(email=email).exists():
           raise forms.ValidationError(f"This {email} is already  used")
       return email

class OrderModelForm(ModelForm):

    class Meta:
        model = Order
        exclude =('product',)
class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'