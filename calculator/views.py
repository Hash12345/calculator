from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import json
from .models import Calculator
from .forms import *
from ast import literal_eval

# Create your views here.
def index(request):
    return render(request, 'index.html')
def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form= CreateUserForm()
        context={'form': form}
        if request.method == "POST":
            
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "account  created for " + user)
                return redirect("index")
    return render(request, 'accounts/register.html', context)
def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username= request.POST.get('username')
            password= request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "username or passord is incorrect")
    return render(request, 'accounts/login.html')
def logout_page(request):
    logout(request)
    return redirect('login')

@login_required
def profile_update_page(request):
    if request.method == "POST":
        form= UpdateUserForm(request.POST, instance=request.user)
        # print(request.POST)
        # user_profile=User.objects.get(pk=request.user.id)
        # user_profile.set_password=request.POST['password']
        # user_profile.save()
        # #user_profile.set_password=request.POST.password
        # print(user_profile)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, "account  Updated successfully")
            return redirect("login")
    elif request.method == "GET":
        form= UpdateUserForm(instance=request.user)
        context={'form': form}
    return render(request, 'accounts/profile.html', context)
@login_required
def calculator_page(request):
    if request.method == "POST":
        data =json.loads(request.body)
        try:
            result = eval(data['expression'])
            Calculator.objects.create(expression=data['expression'], result=result )
            data={
                'success':True,
                'result': result
            }
            return JsonResponse(data, safe=False)
        except ZeroDivisionError:
            Calculator.objects.create(expression=data['expression'], result='undifined: dividing by zero' )
            data={
                'success':False,
                'message': 'undifined: dividing by zero'
            }
            return JsonResponse(data, safe=False)
        except SyntaxError:
            Calculator.objects.create(expression=data['expression'], result='undifined: syntax error' )
            data={
                'success':False,
                'message': 'undifined: syntax error'
            }
            return JsonResponse(data, safe=False)
    return render(request, 'calculator.html')

#
@login_required
def history_page(request):
    calculations=Calculator.objects.all()
    context={'calculations':calculations}
    return render(request, 'history.html',context)

    


