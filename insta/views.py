from django.shortcuts import render,redirect
from insta.models import instaPost
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required(login_url='/admin')
def create(request):
    if request.method=="POST":
        c=request.POST.get('cap')
        i=request.FILES.get('img')
        u=request.user
        obj=instaPost(person=u,caption=c,pic=i)
        obj.save()
        return redirect('instapost')
    return render(request,'create.html')

def home(request):
    objs=instaPost.objects.all()
    if request.method=="POST":
        a=request.POST.get('search')
        results=instaPost.objects.filter(caption__icontains=a)
        return render(request,'home.html',{'posts':results})
    return render(request,'home.html',{'posts':objs})

def login_view(request):
    if request.method=="POST":
        usern=request.POST.get('uname')
        passw=request.POST.get('pass')
        check=authenticate(request,username=usern,password=passw)
        if check is not None:
            login(request,check)
        return redirect('createpost')    
    return render(request,'login.html')



def register_view(request):
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        mail = request.POST.get('email')
        usern = request.POST.get('uname')
        password = request.POST.get('passw')
        cpassword = request.POST.get('cpass')
        if User.objects.filter(username=usern).exists():
            messages.error(request, "Username already exists.")
            return redirect('registerpage')   
        if User.objects.filter(email=mail).exists():
            messages.error(request, "Email is already registered.")
            return redirect('registerpage')     
        if password is None or len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('registerpage')
        if cpassword != password:
            messages.error(request, "Passwords do not match.")
            return redirect('registerpage')      
        obj = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            email=mail,
            username=usern, password=password)
        obj.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('loginpage')
    return render(request, 'register.html')



def logoutView(request):
    logout(request)
    return redirect('loginpage')
