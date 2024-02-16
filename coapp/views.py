from django.shortcuts import redirect, render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from coapp.models import Course,Order,Enroll1
from django.conf import settings
from django.conf.urls.static import static
import razorpay
from django.db.models import Q
# Create your views here.

def reg(request):
    context = {}
    if request.method=='POST':
        fname=request.POST['fname']
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        if fname==""or uname=="" or upass=="" or ucpass=="":
            context['errmsg']="filed cannot be empty"
            return render(request,'reg.html',context)
        elif upass!=ucpass:
            context['errmsg']="password and confirm passsword did not match"
            return render(request,'reg.html',context)
        else:
            try:
                u=User.objects.create(username=uname, email=uname ,first_name=fname)
                u.set_password(upass)
                u.save()
                context['sucess']="user creates succesfully"
                return render(request,'reg.html',context)
            except Exception:
                context['errmsg']="This user alredy existy"
                return render(request,'reg.html',context)

    return render(request,'reg.html')


def login_user(request):
    context = {}
    if request.method == 'POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        if uname=="" or upass=="" :
            context['errmsg']="filed cannot be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            #print(u)
            #print(u.email)
            # print(u.is_superuser)
            # return HttpResponse("in else part")
            if u is not None:
                login(request,u)#start session and store id of logged in user seeion
                return redirect('/home')
            else:
                context['errmsg']="invalid username and password"
                return render(request,'login.html',context)
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('/home')


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def course(request):
    context={}
    p=Course.objects.filter(is_active=True)
    # print(p)
    # print(p[0])
    # print(p[0].description)
    # print(p[0].price)
    # print(p[0].cate)
    context['courses']=p
    return render(request,'courses1.html',context)

# def makepayment(request):
#    c=Course.objects.filter(id=request.user.id)
#    s=0
#    for x in c:
#        s=s.x.cid.price
#        oid=x.s
       
#    return render(request,'payment.html',)

def makepayment(request,cid):
   pass
    

def enroll(request,cid):
    context={}
    context['courses']=Course.objects.filter(id=cid)
    return render(request,'enroll.html',context)



def my_course(request): 
    userid=request.user.id
    e=Enroll1.objects.filter(uid=userid)
    context={}
    context['courses']=e
    return render(request,'mycourse.html',context)

def profile(request):
    first_name = "Anonymous"
    username = "Anonymous"
    email = "N/A"
    if request.user.is_authenticated:
        # Access username and email from the request.user object
        first_name = request.user.first_name
        username = request.user.username
        email = request.user.email
    else:
        # If the user is not authenticated, set default values or handle it as needed
        return redirect('/login')
    
    return render(request, 'profile.html', {'first_name':first_name, 'username': username, 'email': email})
    return render(request,'profile.html')

def dashboard(request):
    return render(request,'dashboard.html')


def addcourse(request, cid):
    if request.user.is_authenticated:
        # print("user is log")
        # return HttpResponse("user log in")
        u=User.objects.filter(id=request.user.id)
        # print(u)
        # print(u[0].username)
        # print(u[0].is_superuser)
        c=Course.objects.filter(id=cid)
        # print(c)
        # return HttpResponse("Course is enroll")
        q1=Q(uid=u[0])
        q2=Q(cid=c[0])
        e=Enroll1.objects.filter(q1&q2)
        print(e)
        n=len(e)
        context={}
        context['courses']=c
        if n==1:
            context['msg']="Course Already Enrolled!!!"
        else:
            e=Enroll1.objects.create(uid=u[0],cid=c[0])
            e.save()
            context['success']="Course Enroll Sucessfully "       
        return render(request,'enroll.html',context)
    else:
        return redirect('/login')



