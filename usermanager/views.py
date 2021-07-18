from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate, logout
from .dataverifier import *
# Create your views here.


def loginview(request):
    if request.method == "POST" and (not request.user.is_authenticated):
        pass
    return redirect('/')

def logoutview(request):
    logout(request)
    return redirect('/')

def RenderLogin(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    return redirect('/')

def RenderSignup(request):
    if not request.user.is_authenticated:
        return render(request,'register.html')
    return redirect('/')

@csrf_exempt
def sendOtp(request):
    otp = randomotpgen()
    r1,messgae = islimitdone(request)
    if r1:
        return sendmail(request=request,otp=otp)
    else:
        return JsonResponse({'result':messgae})

def RegisterUser(request):
    if request.method == "POST":
        name_r = request.POST["name"]
        email_r = request.POST["email"]
        pass_r = request.POST["password"]
        cpass_r = request.POST["cpassword"]
        phone_r = request.POST["phoneno"]
        age_r = request.POST["age"]
        otp_r = request.POST["otp"]
        if not verifyname(name_r):
            return render(request,'confirm.html',{'message':'Invalid Full Name.'})
        if not preprocessmail(email_r):
            return render(request,'confirm.html',{'message':'Incorrect Mail or otp expired.'})
        if not passwordManager(pass_r,cpass_r):
            return render(request,'confirm.html',{'message':'Please use strong password chars,nums,special chars and both password fields should be match.'})
        if not phoneverifier(phone_r):
            return render(request,'confirm.html',{'message':'Invalid Indian Phone Number.'})
        if not verifyAge(age_r):
            return render(request,'confirm.html',{'message':'Age should be in 10-120 years'})
        if otp_match(otp_r,email_r):
            user,cum = savemodels(name_r,email_r,pass_r,phone_r,age_r)
            return render(request,'confirm.html',{'message':'Registration Complete please login.','extlink':True})
        else:
            return render(request,'confirm.html',{'message':'Otp Did not match.'})
        return redirect('/')
    else:
        return redirect('/')

def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user == None:
            return render(request,'confirm.html',{'message':'Invalid Username or Password.'})
        else:
            login(request,user)
            return redirect('/')