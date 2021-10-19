from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, 'homepage/homepage.html', {})

def testhome(request):
    context = {}
    template = "homepage/donotuse.html"
    return render(request, template, context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['userhpn']
        password = request.POST['pwhpn']
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('worksearch')
        else:
            messages.warning(request, "Invalid username or password, please try again")
            return redirect('home')
    else:
        messages.info(request, "Invalid username or password, please try again")
        return redirect('home')

def register_user(request):
    if request.method == 'POST':
        usernamereg = request.POST.get('reguserhp')
        passwordreg = request.POST.get('regpwhpn')
        passwordreg2 = request.POST.get('regpwhpn2')

        if usernamereg is not None:
            if passwordreg != "":
                if passwordreg == passwordreg2:
                    if User.objects.filter(username=usernamereg).exists():
                        messages.warning(request, "Username is already in use")
                        return redirect('home')
                    else:
                        user = User.objects.create_user(username=usernamereg, password=passwordreg)
                        user.save()
                        messages.info(request, "User created successfully")
                        return redirect('home')
                else:
                    messages.info(request, "Passwords do not match")
            if passwordreg == "":
                messages.warning(request, "Something went wrong, please try again")
                print("EMPTY")
                return redirect('home')
        if usernamereg is None:
            messages.warning(request, "Something went wrong, please try again")
            return redirect('home')
    return redirect('home')
