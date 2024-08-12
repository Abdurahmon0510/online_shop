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
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_username(self):
        username = self.data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'This {username} is already exists')
        return username

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        if commit:
            user.save()

        return user