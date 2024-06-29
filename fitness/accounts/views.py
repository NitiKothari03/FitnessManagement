from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import TraineeSignupForm

def trainee_signup(request):
    if request.method == 'POST':
        form = TraineeSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = TraineeSignupForm()
    return render(request, 'registration/signup.html', {'form': form})