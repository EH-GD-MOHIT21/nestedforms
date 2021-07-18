from datetime import time
import smtplib
from email.message import EmailMessage
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from random import randint
from .models import Temporarystorage as TPS,PermanentUserData as PUD,User
from django.utils import timezone


def phoneverifier(phone):
    if len(phone)!=10 or not(phone.isnumeric()):
        return False
    return True


def verifyname(name):
    if len(name) < 4:
        return False
    name = name.split(' ')
    for n in name:
        if not n.isalpha():
            return False
    return True

def preprocessmail(mail):
    if mail.count('@')!=1:
        return False
    if len(mail)<5:
        return False
    try:
        PUD.objects.get(email=mail)
        return False
    except:
        pass
    try:
        obj = TPS.objects.get(email=mail)
        send_time = obj.send_at
        cur_time = timezone.now()
        del_time = str(cur_time-send_time)
        hours,minutes,seconds = map(float,del_time.split(':'))
        if int(hours)!=0:
            return False
        if int(minutes)<=5:
            return True
        return False
    except:
        return False


def passwordManager(p1,p2):
    if len(p1)<8:
        return False
    if p1!=p2:
        return False
    if p1.isnumeric() or p1.isalpha() or p1.isalnum():
        return False
    return True


def otpmatch(original,submitted):
    return original==submitted


def verifyAge(age):
    try:
        age = int(age)
        if age > 8 and age <= 120:
            return True
        else:
            return False
    except:
        return False

def isvalidemail(mail):
    if mail.count('@')!=1:
        return False
    if len(mail)<5:
        return False
    try:
        PUD.objects.get(email=mail)
        return False
    except:
        pass
    return True

@csrf_exempt
def sendmail(request=None,to=None,subject=None,messageper=None,otp=None):
    message = EmailMessage()
    if to!=None:
        message['To'] = to
    else:
        email_l = json.loads(request.body).get('email')
        if not isvalidemail(email_l):
            return JsonResponse({'result':'Invalid Mail Id.'})
        message['To'] = email_l
    if subject!=None:
        message['Subject'] = subject
    else:
        message['Subject'] = "Welcome to NestedForms.com"
    message['From'] = settings.EMAIL_SENDER
    if messageper==None:
        message.set_content(f"Hello User welcome to NestedForms.com Your one time password is {otp} valid for 5 minutes.\n\n\n Happy Form Creating.\n Regards\n NestedForms.com")
    else:
        message.set_content(messageper)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(settings.EMAIL_SENDER, settings.PASS_SENDER)
        server.send_message(message)
        if to==None:
            store_at = TPS(email=email_l,otp=otp)
            store_at.timestampnow
            store_at.save()
            return JsonResponse({'result':'Success'})
        else:
            return 'success'
    except Exception as e:
        print(e)
        if to==None:
            return JsonResponse({'result': 'Email Not Send. Server Error..'})
        else:
            return 'Email Not send.'

def randomotpgen():
    return randint(100000,999999)

def islimitdone(request):
    try:
        User.objects.get(username=json.loads(request.body).get('email'))
        return (False,"Mail id Already Exists")
    except Exception as e:
        # print(e)
        pass
    try:
        obj = TPS.objects.get(email=json.loads(request.body).get('email'))
        send_time = obj.send_at
        cur_time = timezone.now()
        del_time = str(cur_time-send_time)
        hours,minutes,seconds = map(float,del_time.split(':'))
        if int(hours)!=0:
            obj.delete()
            return (True,None)
        if int(minutes)>=5:
            obj.delete()
            # delete record
            return (True,None)
        return (False,'Otp has been send please try again 5 minutes.')
    except:
        return (True,None)

def otp_match(otp,email):
    try:
        obj = TPS.objects.get(email=email)
        if str(otp)!= str(obj.otp):
            return False
        else:
            obj.delete()
            return True
    except:
        return False

def savemodels(name,email,passwd,phone,age):
    user = User(username=email,email=email)
    user.set_password(passwd)
    user.save()
    user_ = PUD(index=user,name=name,phone=phone,age=age)
    user_.save()

    return (user,user_)