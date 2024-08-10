from django import forms
from django.contrib.auth.forms import UserCreationForm
from online_shop.models import Comment, Order, Product
from django.contrib.auth.models import User


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =('product',)

    def clean_email(self):
       email=self.cleaned_data.get('email')
       if Comment.objects.filter(email=email).exists():
           raise forms.ValidationError(f"This {email} is already  used")
       return email

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude =('product',)
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'quantity', 'rating', 'discount','slug']

class LoginFrom(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    # def clean_username(self):
    #     username=self.data.get('username')
    #     if not User.objects.filter(username=username).exists():
    #         raise forms.ValidationError(f'That user {username} not found')
    #
    #     return username

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            self.add_error('password2', 'Passwords do not match')
