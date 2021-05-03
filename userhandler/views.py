from django.shortcuts import render,redirect
from .models import registration_form
from django.views.decorators.csrf import csrf_exempt
from random import randrange
from django.http import HttpResponse,JsonResponse
import json
import smtplib
from email.message import EmailMessage
from datetime import datetime
# Create your views here.

otp_ = "hwfj#########jhvjaxs%444&&&&&&&&&+++++_)((*&%^%$$$#@!))  cd sn dcjbhcbjhj    j jdbhbhjcbfjnbkdfdlk';,nfb vnvjkc"
cur_min = otp_


def register(request):
    
    return render(request,'register.html')

def login(request):
    
    return render(request,'login.html')

def mailer(to,otp):
    sender_mail = "no.reply.python.py@gmail.com"   
    password_sender = "qwerty@123"

    message = EmailMessage()
    message['To'] = to
    message['From'] = sender_mail
    message['Subject'] = "Welcome User to NestedForms.com"
    message.set_content(f"Hello User welcome to NestedForms.com Your one time password is {otp} valid for 5 minutes.\n\n\n Happy Form Creating.\n Regards\n NestedForms.com")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, password_sender)
        server.send_message(message)
        return JsonResponse({'result':'Success'})
    except Exception as e:
        return JsonResponse({'result': e})

@csrf_exempt
def otpgen(request):
    mail = json.loads(request.body).get('email')
    global otp_,userkiasliyat,cur_min
    userkiasliyat = mail
    cur_min = datetime.now()
    otp_ = randrange(100000,999999)
    if mail == '' or mail is None:
        return JsonResponse({'result':'Failure'})
    return mailer(mail,otp_)

def verify(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['pass']
        data = registration_form.objects.filter(email=user,password=password)
        for da in data:
            if user == da.email and password == da.password and len(data)==1:
                return render(request,'confirm.html',{'special':'yes'})
            else:
                return render(request,'confirm.html',{'message':'Invalid credentials'})
        return render(request,'confirm.html',{'message':'Invalid credentials'})
    else:
        return redirect('/login')

def checkuser(request=None,name=None,email=None,password=None,cpass=None,phoneno=None,age=None,otp=None):
    global otp_,cur_min
    cur_min2 = datetime.now()
    cur_min = datetime.strptime(str(cur_min), '%Y-%m-%d %H:%M:%S.%f')
    timegap = str(cur_min2-cur_min)
    times = timegap.split(':')
    if int(times[0])!=0 or int(times[1])>1:
        otp_ = randrange(100000,999999)
        return render(request,'confirm.html',{'message':'Time limit Exeeced Session Expire please retry.'})

    if name=='' or email=='' or password=='' or cpass=='' or phoneno=='' or age=='' or otp=='':
        return render(request,'confirm.html',{'message':'Invalid credentials'})

    if userkiasliyat!=email:
        return render(request,'confirm.html',{'message':'Email Id is changed By user.'})
        
    try:
        if int(age)>13 and int(age)<100:
            pass
        else:
            return render(request,'confirm.html',{'message':'Invalid Age should be at least 13 and max 100.'})
    except:
        return render(request,'confirm.html',{'message':'Age Should be integer.'})
    if len(password)<8:
        return render(request,'confirm.html',{'message':'Please set a password of atleast 8 characters.'})
    elif password!=cpass:
        return render(request,'confirm.html',{'message':"Password and Repassword Didn't match."})
    
    if str(otp)!=str(otp_):
        return render(request,'confirm.html',{'message':"Otp didn't match."})
    if len(name)<=4:
        return render(request,'confirm.html',{'message':'Inappropriate Name please Enter Real Data.'})
    try:
        a = email.split('@')
        if len(a)!=2 or email[-1]=='@' or email[-2]=='@' or email[0]=='@' or email[1]=='@':
            return render(request,'confirm.html',{'message':'Email Id is not correct'})
        b = email.split('.')
        if len(b)>3 or email[-1]=='.' or email[-2]=='.' or email[0]=='.' or email[1]=='.':
            return render(request,'confirm.html',{'message':'Email Id is not correct'})
    except:
        return render(request,'confirm.html',{'message':'Email Id is not correct'})

    if not phoneno.isnumeric() or len(phoneno)!=10:
        return render(request,'confirm.html',{'message':'Phone number not correct.'})

    
        
    
    otp_ = randrange(100000,999999)

    if len(registration_form.objects.filter(email=email)):
        return render(request,'confirm.html',{'message':'Email already exists.'})
    mydatabase = registration_form(name=name,email=email,password=password,phoneno=phoneno,age=age)
    mydatabase.save()
    
    
    return render(request,'confirm.html',{'message':'Received Request for Registration.','extlink':'yes'})

def verifyuser(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    cpass = request.POST['cpassword']
    phoneno = request.POST['phoneno']
    age = request.POST['age']
    otp = request.POST['otp']
    return checkuser(request,name,email,password,cpass,phoneno,age,otp)
