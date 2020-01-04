from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# import django build model for Login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    # Telling it have been registered or not
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save User Form to Database
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()

            # 這裡加入commit=False的原因是因為防止對user_form.save()覆蓋而造成error
            # 所以可以使用下面那一行
            profile = profile_form.save(commit=False)
            # Because we need connect the User model to the profile_pic
            # And connect the information from the User Profile form to the actual user
            profile.user = user
            '''
            request.FILES --> A dictionary-like object containing all uploaded files. Each key in FILES is the name from the <input type="file" name="">. Each value in FILES is an UploadedFile.
            **FILES will only contain data if the request method was POST and the <form> that posted to the request had enctype="multipart/form-data". Otherwise, FILES will be a blank dictionary-like object.
            '''
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

# 創建class的時候應避免與import的東西同名
def user_login(request):

    if request.method == 'POST':
        # **抓取login.html中input的name，所以名稱要正確
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not actived")
        else:
            print('Someone tried to login and faild!')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def specical(request):
    return HttpResponse('You are logged in, Nice!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
