from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from Opythonapp.forms import UserProfileCreation
from Opythonapp.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def header_view(request):
    return render(request,'header.html')
def user_reg_view(request):
    form=UserProfileCreation()
    msg=''
    if request.method=="POST":
        try:
            form = UserProfileCreation(data=request.POST)
            if form.is_valid():
                form.save()
                form.instance.password = make_password(form.data["password"])
                form.instance.save()
                msg='User created successfully'
        except Exception as err:
            print("error"),err
            msg=form._errors
    return render(request,'user_registration.html',{"form":form,"message":msg})
def login_view(request):
    form=AuthenticationForm()
    msg=''
    if request.method=="POST":
        data = request.POST
        username=data["username"]
        if "@" in username and "." in username:
            user=UserProfile.objects.filter(email=username)
            if not user:
                msg="Invalid credentials, please enter correct username or password"
                return render(request,'login.html',{'form':form,"message":msg})
            else:
                username=user[0].username
        password=data["password"]
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            request.session["username"] = user.first_name
            msg = "LOGIN SUCCESS"
            next_url = request.GET.get ("next", None)
            if next_url:
                return redirect (next_url)
            return redirect ("/home/")
        else:
            msg = "Invalid creadentials"
    return render (request, "login.html",
                   {"form": form, "message": msg})
def signout_view(request):
	if request.method=="POST":
		logout(request)
		return redirect("/home")
	return render(request, "signout.html")
