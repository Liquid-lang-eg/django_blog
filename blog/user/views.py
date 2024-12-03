from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserCreationForm
from .models import User
from django.urls import reverse_lazy
from .forms import SignUpForm

def sign_in_view(request):
    if request.user.is_authenticated:
        return redirect('blog:post_list')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('blog:post_list')

    elif request.method == 'GET':
        form = AuthenticationForm(request)

    return render(
        request,
        'sign_in.html',
        context={'form': form}
    )


def logout_view(request):
    logout(request)
    return redirect('blog:post_list')


def sign_up_view(request):
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:sign_in')

    elif request.method == 'GET':
        form = SignUpForm()

    return render(
        request,
        'sign_up.html',
        context={'form': form}
    )

# class SignUpView(CreateView):
#
#     model = User
#     template_name = 'sign_up.html'
#     success_url = reverse_lazy('user:sign_in')
