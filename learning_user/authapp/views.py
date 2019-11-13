from django.shortcuts import render
from authapp.forms import UserForm, UserProfileInfoForm

# 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404  
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'authapp/index.htm')

@login_required
def special(request):
    return HttpResponse('You are logged in {}'.format(username))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # Grab d user_form and save into d database
            user.set_password(user.password)
            # This is simple hashing d password. it goes in to setting.py file & set it as a hash
            user.save()
            # saving d hash password into d database

            profile = profile_form.save(commit = False)
            # I don't want to summit to the database yet in other not to overwrite user
            # This also helps to prevent collision error. that is having duplicate profile
            profile.user = user
            # This sets up d oneToone Relationship in d models.py file
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'authapp/registration.htm',
                {'user_form': user_form, 'profile_form':profile_form,
                    'registered': registered})

def user_login(request):

    if request.method == "POST":
        # User has actually filled out d Login info
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password= password)
        # django authenticate this user for you

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            print('Some tried to login and failed! ')
            print('Username: {} and password {}'.format(username,password))
            return HttpResponse("invalid login details supplied ")
    else:
        return render(request, 'authapp/login.htm',  {})
            

            



