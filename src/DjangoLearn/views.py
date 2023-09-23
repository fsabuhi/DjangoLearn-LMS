from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from .forms import CustomAuthenticationForm
from .forms import UserForm
from django.contrib.auth.models import User
@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            # Redirect to the home page if the user is authenticated
            return HttpResponseRedirect('/index/')
        else:
            # Add an error message to the form if the authentication fails
            form.add_error(None, '')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@csrf_exempt
def registration(request): 
    form = UserForm(request.POST)
    if form.is_valid():
        User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password'])
        response = HttpResponseRedirect(f'/login/')
        return response

@login_required()
def index(request):
    return render(request, 'loggedin.html')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect('/index/')
    # response['Location'] = '/loggedin/'
    return response