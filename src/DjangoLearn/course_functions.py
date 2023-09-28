from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CourseForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import CourseModel
@login_required
@csrf_exempt
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        print('hahas')
        if form.is_valid():
            
            print(form.cleaned_data['name'])
            course = CourseModel.objects.create(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
            course.save()
            response = HttpResponseRedirect(f'/courses/')
            return response
    else:
        form = CourseForm()
    return HttpResponseRedirect(f'/courses/')

@login_required
def delete_course(request, name):
    course = CourseModel.objects.get(name=name)
    course.delete()
    return HttpResponseRedirect(f'/courses/')