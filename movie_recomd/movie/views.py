from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from .models import Movie, Review
from .forms import MovieForm, ReviewForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout as django_logout


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def profile(request):
    user = request.user
    movies = Movie.objects.filter(added_by=user)  # Retrieve movies added by the user
    return render(request, 'profile.html', {'user': user, 'movies': movies})


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews})


def post_review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            messages.success(request, 'Your review has been posted successfully.')
            return redirect('movie_detail', pk=pk)
        else:
            messages.error(request, 'Failed to post review. Please correct the errors.')
    else:
        form = ReviewForm()
    return render(request, 'post_review.html', {'form': form, 'movie': movie})


def search(request):
    query = request.GET.get('q')
    movies = Movie.objects.filter(title__icontains=query) | Movie.objects.filter(description__icontains=query)
    return render(request, 'search_results.html', {'movies': movies})


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def your_view(request):
    # Create a new Movie object
    movie = Movie.objects.create(title="Your Movie Title", description="Your movie description")

    # Now you can access its primary key (pk)
    movie_pk = movie.pk

    # Pass the movie object and its primary key to the template context
    return render(request, 'your_template.html', {'movie': movie, 'movie_pk': movie_pk})


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after successful edit
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form})


def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        # If the request method is POST, delete the movie and redirect to a success URL
        movie.delete()
        return redirect('profile')  # Assuming 'profile' is the name of your profile view
    # If the request method is GET, render a confirmation page
    return render(request, 'delete_movie.html', {'movie': movie})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('profile')
        else:
            # Return an invalid login error message
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout(request):
    django_logout(request)
    return redirect('home')
