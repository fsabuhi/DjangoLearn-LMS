from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from .forms import CustomAuthenticationForm
from .forms import UserForm
from .models import UserModel
from .models import CourseModel
from django.shortcuts import redirect
from django.contrib.auth.models import User
@csrf_exempt
def auth(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            # Check the user's credentials
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in and redirect to the home page
                login(request, user)
                return redirect('index/')
            else:
                # Add an error message to the form if the authentication fails
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request): 
    return render(request, 'register.html')


@login_required()
def index(request):
    user_model = UserModel.objects.get(user=request.user)
    user_type = user_model.type
    return render(request, 'loggedin.html', {'user_type': user_type})
def login_page(request):
    return render(request, 'login.html')    

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect('/index/')
    # response['Location'] = '/loggedin/'
    return response

@csrf_exempt
def registration(request): 
    form = UserForm(request.POST)
    if form.is_valid():
        user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password'])
        print(form.cleaned_data['type'])
        user_model = UserModel.objects.create(user=user, type=form.cleaned_data['type'])
        response = HttpResponseRedirect(f'/login/')
        return response
    
@login_required
def courses(request):
    user_model = UserModel.objects.get(user=request.user)
    user_type = user_model.type
    courses = CourseModel.objects.all().values()
    # if user_type == 'teacher':
    return render(request, 'courses.html', {'courses':courses,'user':user_model})
    # else:
    #     return HttpResponse('You are not authorized to view this page')



def course_form(request):
    return render(request, 'course_form.html')