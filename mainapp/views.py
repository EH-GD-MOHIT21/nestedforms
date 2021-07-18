from django.shortcuts import render,redirect
from .models import formpublicdata
from .models import responses as form_responses
from django.views.decorators.csrf import csrf_exempt
from random import choice



# Create your views here.


def home(request):
    return render(request,'home.html')


def saveresponse(request,formid=None):
    if not request.user.is_authenticated:
        return render(request,'confirm.html',{'message':'Please Login to fill a form.'})
    if request.method == "GET":
        return redirect('/')
    name = request.POST['name']
    mail = request.user.username
    phone = request.POST['phone']
    address = request.POST['address']
    delimitor = "@*[=m!@}$o%^:h&8*i-;t"
    responses = []
    i = 0
    while True:
        try:
            option = request.POST[str(i)]
            responses.append(option)
            i+=1
        except:
            break
    responses = delimitor.join(responses)
    if len(form_responses.objects.filter(code=formid,mail=mail)) or len(form_responses.objects.filter(code=formid,phone=phone)):
        return render(request,'confirm.html',{'message':"You've already responded"})
    temp = form_responses(code=formid,name=name,mail=mail,phone=phone,address=address,responses=responses)
    temp.save()
    return render(request,'confirm.html')

def fillform(request,formid=None):
    if not request.user.is_authenticated:
        return redirect('/login')
    if formid == None:
        return redirect('/login')
    try:
        form_responses.objects.get(code=formid,mail=request.user.username)
        return render(request,'confirm.html',{'message':"You've Already Responded."})
    except:
        pass
    myformdata = formpublicdata.objects.filter(code=formid)
    if len(myformdata)==1:
        delimitor = "@*[=m!@}$o%^:h&8*i-;t"
        for element in myformdata:
            element.questions = element.questions.split(delimitor)
            element.option1 = element.option1.split(delimitor)
            element.option2 = element.option2.split(delimitor)
            element.option3 = element.option3.split(delimitor)
            element.option4 = element.option4.split(delimitor)
            main_list = zip(element.questions,element.option1,element.option2,element.option3,element.option4)
            content = {
                'mainlist':main_list
            }
            return render(request,'quiz.html',{'title':element.title,'desc':element.desc,'creator':element.creator,'mail':element.mail,'content':content,'formid':formid})
    else:
        return redirect('/login')

def createform(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect('/login')

def generateaunicode():
    varsptoken = ''
    alphas = ['-','_','0','1','2','3','4','5','6','7','8','9']
    for i in range(26):
        alphas.append(chr(65+i))
        alphas.append(chr(97+i))
    for i in range(81):
        varsptoken += choice(alphas)

    return (varsptoken)

@csrf_exempt
def savedetails(request):
    if not request.user.is_authenticated:
        return render(request,'confirm.html',{'message':'Please Login And Try Again.'})
    if request.method == "GET":
        return redirect('/')

    personalcode = generateaunicode()
    
    title = request.POST['formtitle']
    mail = request.user.username
    creatorname = request.POST['creatorname']
    desc = request.POST['formdesc']
    i = 0
    questions = []
    option1 = []
    option2 = []
    option3 = []
    option4 = []
    while True:
        try:
            question = request.POST[f'question{i}']
            op1 = request.POST[f'option1{i}']
            op2 = request.POST[f'option2{i}']
            op3 = request.POST[f'option3{i}']
            op4 = request.POST[f'option4{i}']
            questions.append(question)
            option1.append(op1)
            option2.append(op2)
            option3.append(op3)
            option4.append(op4)
            i+=1
        except:
            break

        if i > 2000:
            return render(request,'logshower.html',{'formid': 'sorry but you cannot make so much questions limit is 2000.'})
    delimitor = "@*[=m!@}$o%^:h&8*i-;t"
    questions = delimitor.join(questions)
    option1 = delimitor.join(option1)
    option2 = delimitor.join(option2)
    option3 = delimitor.join(option3)
    option4 = delimitor.join(option4)

    
    mytimecalculator = 0
    while(len(formpublicdata.objects.filter(code=personalcode))):
        personalcode = generateaunicode()
        mytimecalculator +=1
        if mytimecalculator > 10000:
            return render(request,'logshower.html',{'formid': 'sorry but we are unable to process your request'})
    
    temp = formpublicdata(title=title,mail=mail,creator=creatorname,desc=desc,questions=questions,option1=option1,option2=option2,option3=option3,option4=option4,code=personalcode)
    temp.save()
    return render(request,'logshower.html',{'formid':personalcode,'message':'success'})

@csrf_exempt
def getformbyid(request):
    formid = request.POST['formtoken']
    myformdata = formpublicdata.objects.filter(code=formid)
    if len(myformdata)==1:
        delimitor = "@*[=m!@}$o%^:h&8*i-;t"
        for element in myformdata:
            element.questions = element.questions.split(delimitor)
            element.option1 = element.option1.split(delimitor)
            element.option2 = element.option2.split(delimitor)
            element.option3 = element.option3.split(delimitor)
            element.option4 = element.option4.split(delimitor)
            main_list = zip(element.questions,element.option1,element.option2,element.option3,element.option4)
            content = {
                'mainlist':main_list
            }
            return render(request,'quiz.html',{'title':element.title,'desc':element.desc,'creator':element.creator,'mail':element.mail,'content':content,'formid':formid})
    else:
        return render(request,'confirm.html',{'special':'yes'})


def fillformuser(request):
    if request.user.is_authenticated:
        return render(request,'confirm.html',{'special':'yes'})
    else:
        return redirect('/login')


def showresponsepage(request,formid=None,email=None):
    if not request.user.is_authenticated:
        return render(request,'confirm.html',{'message':'Please Login to authenticate.'})
    try:
        email = request.GET["email"]
        delimitor = "@*[=m!@}$o%^:h&8*i-;t"
        form = formpublicdata.objects.get(code=formid)
        title = form.title
        desc = form.desc
        author = form.creator
        contact = form.mail
        responses_obj = form_responses.objects.get(code=formid,mail=email)
        # if not res_len:
        #     return redirect('/')
        questions = form.questions
        option1 = form.option1
        option2 = form.option2
        option3 = form.option3
        option4 = form.option4
        questions = questions.split(delimitor)
        option1 = option1.split(delimitor)
        option2 = option2.split(delimitor)
        option3 = option3.split(delimitor)
        option4 = option4.split(delimitor)
        responses = responses_obj.responses
        responses = responses.split(delimitor)
        data = zip(questions,option1,option2,option3,option4,responses)
        # pick qus from formpublic data

        username = responses_obj.name
        mail = responses_obj.mail
        phone = responses_obj.phone
        address = responses_obj.address
        # print(request.user.is_superuser)
        
        # permission <<<->>>

        if (email == request.user.username):
            return render(request,'showresponses.html',{'title':title,'desc':desc,'author':author,'contact':contact,'data':data,'username':username,'mail':mail,'phone':phone,'address':address})
        if (form.mail==request.user.username):
            return render(request,'showresponses.html',{'title':title,'desc':desc,'author':author,'contact':contact,'data':data,'username':username,'mail':mail,'phone':phone,'address':address})
        if (request.user.is_superuser):
            return render(request,'showresponses.html',{'title':title,'desc':desc,'author':author,'contact':contact,'data':data,'username':username,'mail':mail,'phone':phone,'address':address})
        
        return render(request,'confirm.html',{'message':'You Cannot see someone others responses.'})

    except Exception as e:
        # print(e)
        return redirect('/')
    

def creatorpageview(request):
    if request.user.is_authenticated:
        forms = formpublicdata.objects.filter(mail=request.user.username)
        formids = []
        for form in forms:
            formids.append(form.code)
        total_res = []
        responses = []
        for ids in formids:
            temp = []
            data = form_responses.objects.filter(code=ids)
            for dat in data:
                temp.append(dat.mail)
            responses.append(temp)
            total_res.append(len(data))
        data = zip(formids,total_res)
        # print(responses)
        for form in forms:
            return render(request,'creator.html',{'data':data,'mail':request.user.username,'resdata':responses})
        return render(request,'confirm.html',{'message':'You Have Not created Any forms please create some.'})
    else:
        return redirect('/')