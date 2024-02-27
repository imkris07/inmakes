from .models import Movie, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address', label='Email address')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        # Add custom validation rules for first name
        if len(first_name) < 2:
            raise ValidationError("First name must be at least 2 characters long.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        # Add custom validation rules for last name
        if len(last_name) < 2:
            raise ValidationError("Last name must be at least 2 characters long.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Add custom validation rules for email
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Add custom password validation rules
        if len(password1) < 8:
            raise ValidationError("Your password must contain at least 8 characters.")
        if password1.isdigit():
            raise ValidationError("Your password can't be entirely numeric.")
        return password1


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'review_text': forms.Textarea(attrs={'rows': 3}),
        }
