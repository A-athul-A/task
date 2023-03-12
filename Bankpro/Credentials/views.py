from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Register



# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            print("Login success")
            return render(request,'linktoreg.html')
        else:
            messages.info(request, "Incorrect username or password")
            return redirect('login')


    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if username:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password
                    )
                    if user is not None:
                        user.save()
                        return redirect('login')
                    else:

                        return redirect('signup')
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password mismatch')
            return redirect('signup')
        messages.info(request, "Please enter username and password")

    return render(request, 'signup.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        # age = request.POST.get()
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        mob = request.POST.get('mob', '')
        mail = request.POST.get('mail', '')
        address = request.POST.get('address','')
        branch = request.POST.get('branch','')
        district = request.POST.get('district','')
        actype = request.POST.get('actype', '')
        mp = request.POST.get('mp', '')
        if name and dob and gender and mob and mail and address and branch and district and actype and mp:
            regi = Register(
                name=name,
                dob=dob,
                gender=gender,
                mob=mob,
                mail=mail,
                address=address,
                branch=branch,
                district=district,
                actype=actype,
                mp=mp,
            )
            regi.save()
            messages.info(request, "Application accepted")
            auth.logout(request)
        else:
            messages.info(request, "Please enter details")
    return render(request, 'register.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')
#     return render(request, 'signup.html')
