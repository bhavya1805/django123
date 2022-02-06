from django.contrib.auth.forms import UserCreationForm
from newbook.models import CustomUser
from django import forms
from newbook.models import Book
class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('email','phone','address')
