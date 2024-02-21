from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login, logout
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def update(request, pk):
    mymember= get_object_or_404(User, pk=pk)
  
    return render(request, 'users/update.html', {
        'mymember': mymember
    })
    
def updaterecord(request, pk):
    
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    member = get_object_or_404(User, pk=pk)
    member.first_name = first_name
    member.last_name = last_name
    member.email = email
    member.save()
    return HttpResponseRedirect(reverse('users:index'))

    


def registerPage(request):
    pass
    # form = UserCreationForm()
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            
    # context = {'form': form}
    # return render(request, 'users/register1.html', context)
@login_required
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            login(request, user)
            
            return HttpResponseRedirect(reverse("apps:indexApp"))
        else:
            messages.error(request, "Your username or password are not correct. Try login again.!")
            render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "you log out successful!")
    return render(request, "users/login.html", {
        "message": "Logged Out"
    })


def resetpwd(request):
    return render(request,'users/reset_password.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['username']
            form.cleaned_data['email']
            form.cleaned_data['password1']
            form.save()
            messages.success(request, "You have create an account successful. Try login now.")
            return HttpResponseRedirect(reverse('users:index'))
        else:
            messages.error(request, "you're information is not valid, try again.")
            return render(request, 'users/register.html', {
                'form': form
            })

    return render(request, 'users/register.html',{
            'form': RegistrationForm()
        })




    
    