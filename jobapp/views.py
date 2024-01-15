from django.shortcuts import render,redirect
from . models import JobSeeker,Login,Recruiter,Enquiry,Jobs,Apply,News
from datetime import date
# Create your views here.
def index(request):
    nw=News.objects.all()
    return render(request,'index.html',{'nw':nw})

def about(request):
    return render(request,'about.html')

def jobseekerreg(request):
    return render(request,'jobseekerreg.html')

def employerreg(request):
    return render(request,'employerreg.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return  render(request,'login.html')


def jsreg(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    dob=request.POST['dob']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    keyskills=request.POST['keyskills']
    image=request.FILES['image']
    regdate=date.today()
    password=request.POST['password']
    usertype='jobseeker'
    js=JobSeeker(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,dob=dob,qualification=qualification,experience=experience,keyskills=keyskills,image=image,regdate=regdate)
    log=Login(userid=emailaddress,password=password,usertype=usertype)
    js.save()
    log.save()
    msg='Registration is Succcessfully'
    return render(request,'jobseekerreg.html',{'msg':msg})



def ereg(request):
    firm_name=request.POST['firm_name']
    photo = request.FILES['photo']
    firm_address=request.POST['firm_address']
    cpname=request.POST['cpname']
    cpcontactno=request.POST['cpcontactno']
    cpemailaddress=request.POST['cpemailaddress']
    aadharno=request.POST['aadharno']
    panno=request.POST['panno']
    gstno=request.POST['gstno']
    regdate=date.today()
    password=request.POST['password']
    usertype='employer'
    r=Recruiter(firm_name=firm_name,photo=photo,firm_address=firm_address,cpname=cpname,cpcontactno=cpcontactno,cpemailaddress=cpemailaddress,aadharno=aadharno,panno=panno,gstno=gstno,regdate=regdate)
    log=Login(userid=cpemailaddress,password=password,usertype=usertype)
    r.save()
    log.save()
    msg='Registration is Succesufully'
    return  render(request,'employerreg.html',{'msg':msg})

def saveenq(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    posteddate=date.today()
    enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,posteddate=posteddate)
    enq.save()
    msg='Enquiry is submitted'
    return render(request,'contact.html',{'msg':msg})

def validate(request):
    userid=request.POST['userid']
    password=request.POST['password']
    usertype=request.POST['usertype']
    try:
        obj=Login.objects.get(userid=userid,password=password,usertype=usertype)
        if obj.usertype=='employer':
            request.session['employer']=userid
            return redirect('emphome')
        elif obj.usertype=='jobseeker':
            request.session['jobseeker']=userid
            return redirect('jobhome')
        elif obj.usertype=='admin':
            request.session['admin']=userid
            return redirect('adminhome')
    except:
        msg='Invalid login credentials!!..Please enter correct details'
    return render(request,'login.html',{'msg':msg})


def emplogout(request):
    request.session['employer'] = None
    return redirect('/')


def emphome(request):
    emp = Recruiter.objects.filter(cpemailaddress=request.session['employer']).all()
    return  render(request,'emphome.html',{'emp':emp})

def postjob(request):
    try:
        if request.session['employer']:
            return render(request,'postjob.html')
    except:
        return render(request,'login.html')


def empchangepassword(request):
    try:
        if request.session['employer']:
            return render(request,'empchangepassword.html')
    except:
        return render(request,'login.html')


def pjob(request):
    obj=Recruiter.objects.get(cpemailaddress=request.session['employer'])
    firmname=obj.firm_name
    emailaddress=obj.cpemailaddress
    jobtitle=request.POST['jobtitle']
    start_date=request.POST['start_date']
    end_date=request.POST['end_date']
    img=request.FILES['img']
    skills=request.POST['skills']
    jobtype=request.POST['jobtype']
    jobdesc=request.POST['jobdesc']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    location=request.POST['location']
    salarypa=request.POST['salarypa']
    posteddate=date.today()
    j=Jobs(employer=obj,firmname=firmname,emailaddress=emailaddress,jobtitle=jobtitle,start_date=start_date,end_date=end_date,img=img,skills=skills,jobtype=jobtype,jobdesc=jobdesc,qualification=qualification,experience=experience,location=location,salarypa=salarypa,posteddate=posteddate)
    j.save()
    msg='Job is posted'
    return render(request,'postjob.html',{'msg':msg})


def joblist(request):
   if not request.user.is_authenticated:
       return redirect('login')
   obj = Recruiter.objects.get(cpemailaddress=request.session['employer'])
   job=Jobs.objects.filter(employer=obj).order_by('-start_date')
   return render(request,'joblist.html',{'job':job})



def edit_jobdetail(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    alert=""
    obj = Recruiter.objects.get(cpemailaddress=request.session['employer'])
    job=Jobs.objects.get(id=id)
    if request.method == 'POST':
        jt=request.POST['jobtitle']
        sd = request.POST['start_date']
        ed = request.POST['end_date']
        jobtype = request.POST['jobtype']
        qualification = request.POST['qualification']
        experience = request.POST['experience']
        skills = request.POST['skills']
        location = request.POST['location']
        salarypa = request.POST['salarypa']
        jobdesc = request.POST['jobdesc']
        job.jobtitle=jt
        job.jobtype=jobtype
        job.qualification=qualification
        job.experience=experience
        job.skills=skills
        job.location=location
        job.salarypa=salarypa
        job.jobdesc=jobdesc
        try:
            job.save()
            alert=False
        except:
            alert=True
        if sd:
            try:
                job.start_date=sd
                job.save()
            except:
                pass
        else:
            pass
        if ed:
            try:
                job.end_date=ed
                job.save()
            except:
                pass
        else:
            pass
    d={'job':job,'alert':alert}
    return render(request,'edit_jobdetail.html',d)

def applyjob(request):
    if request.session['jobseeker']:
        jb=Jobs.objects.all().order_by('-start_date')
        st = JobSeeker.objects.get(emailaddress=request.session['jobseeker'])
        apply=Apply.objects.filter(student=st)
        data=[]
        for i in apply:
            data.append(i.job.id)
        d={'jb':jb,'data':data}
        return render(request,'applyjob.html',d)

def job_detail(request,id):
    job = Jobs.objects.get(id=id)
    return render(request, 'job_detail.html',{'job':job})

def applyforjob(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    obj = JobSeeker.objects.get(emailaddress=request.session['jobseeker'])
    job=Jobs.objects.get(id=id)
    s_d=job.start_date
    e_d=job.end_date
    d=date.today()
    if e_d < d:
        error="close"
    elif s_d > d:
        error="notopen"
    else:
        if request.method == 'POST':
            empemailaddress = job.emailaddress
            rs = request.FILES['resume']
            a=Apply(job=job,student=obj,empemailaddress=empemailaddress,resume=rs,applydate=date.today())
            a.save()
            error="done"
    d={'error':error}
    return render(request,'applyforjob.html',d)


def manageapp(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Apply.objects.filter(empemailaddress=request.session['employer']).all()
    #data=Apply.objects.all().order_by('-applydate')
    d={'data':data}
    return render(request,'manageapp.html',d)



def delete_job(request,id):
    obj=Jobs.objects.get(id=id)
    obj.delete()
    return redirect('joblist')



def change_companylogo(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    obj = Recruiter.objects.get(cpemailaddress=request.session['employer'])
    job=Jobs.objects.get(id=id)
    if request.method == 'POST':
        cn = request.FILES['logo']
        job.img=cn
        job.save()
        alert=True
        return render(request,'change_companylogo.html',{'alert':alert})
    return render(request, 'change_companylogo.html', {'job': job})


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    obj = JobSeeker.objects.get(emailaddress=request.session['jobseeker'])
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        contactno = request.POST['contactno']
        emailaddress = request.POST['emailaddress']
        qualification = request.POST['qualification']
        obj.name=name
        obj.contactno=contactno
        obj.emailaddress=emailaddress
        obj.gender=gender
        obj.qualification=qualification
        obj.save()
        try:
            i=request.FILES['image']
            obj.image=i
            obj.save()
        except:
            pass
    d = {'obj': obj}
    return render(request,'user_profile.html',d)



def emp_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    obj = Recruiter.objects.get(cpemailaddress=request.session['employer'])
    if request.method == 'POST':
        n = request.POST['cpname']
        fn = request.POST['firm_name']
        cn = request.POST['cpcontactno']
        e = request.POST['cpemailaddress']
        fa = request.POST['firm_address']
        obj.cpname=n
        obj.cpcontactno=cn
        obj.cpemailaddress=e
        obj.firm_name=fn
        obj.firm_address=fa
        obj.save()
        try:
            i=request.FILES['photo']
            obj.photo=i
            obj.save()
        except:
            pass
    d = {'obj': obj}
    return render(request, 'emp_profile.html',d)




def latest_jobs(request):
    jl=Jobs.objects.all().order_by('-start_date')
    return render(request,'latest_jobs.html',{'jl':jl})


def empchangepwd(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    msg=''
    if newpassword!=confirmpassword:
        msg=msg+'New password and confirm password should be same'
        return render(request,'empchangepassword.html',{'msg':msg})
    userid=request.session['employer']
    usertype='employer'
    try:
        obj=Login.objects.get(userid=userid,password=oldpassword,usertype=usertype)
        log=Login(userid=userid,password=newpassword,usertype=usertype)
        log.save()
        return redirect('emplogout')
    except:
        msg=msg+'Old password does not match'
    return render(request,'empchangepassword.html',{'msg':msg})



def jobhome(request):
    js = JobSeeker.objects.filter(emailaddress=request.session['jobseeker']).all()
    return render(request,'jobhome.html',{'js':js})



def jobchangepassword(request):
    try:
        if request.session['jobseeker']:
            return render(request,'jobchangepassword.html')
    except:
        return render(request,'login.html')

def adminchangepass(request):
    try:
        if request.session['admin']:
            return render(request,'adminchangepass.html')
    except:
        return render(request,'login.html')

def joblogout(request):
    request.session['jobseeker']=None
    return redirect('/')



def jobchangepwd(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    msg=''
    if newpassword!=confirmpassword:
        msg=msg+'New password and confirm password should be same'
        return render(request,'jobchangepassword.html',{'msg':msg})
    userid=request.session['jobseeker']
    try:
        obj=Login.objects.get(userid=userid,password=oldpassword)
        Login.objects.filter(userid=userid).update(password=newpassword)
        return redirect('joblogout')
    except:
        msg=msg+'Old password does not match'
    return render(request,'jobchangepassword.html',{'msg':msg})

def adminchangepwd(request):
    o=request.POST['o']
    n=request.POST['n']
    c=request.POST['c']
    msg=''
    if n!=c:
        msg=msg+"New password and confirm password should be same"
        return render(request,'adminchangepass.html',{'msg':msg})
    userid=request.session['admin']
    try:
        obj=Login.objects.get(userid=userid,password=o)
        Login.objects.filter(userid=userid).update(password=n)
        return redirect('adminlogout')
    except:
        msg=msg+'Old password does not match'
    return render(request,'adminchangepass.html',{'msg':msg})



def jsprofile(request,id):
    obj=Apply.objects.get(id=id)
    return render(request,'jsprofile.html',{'obj':obj})

def adminhome(request):
    nw=News.objects.all()
    return render(request,'adminhome.html',{'nw':nw})

def adminlogout(request):
    request.session['admin']=None
    return redirect('/')

def enquiries(request):
    try:
        if request.session['admin']:
            enq=Enquiry.objects.all()
            return render(request,'enquiries.html',{'enq':enq})
    except:
        return render(request,'login.html')

def jobseekers(request):
    try:
        if request.session['admin']:
            js=JobSeeker.objects.all()
            return render(request,'jobseekers.html',{'js':js})
    except:
        return render(request,'login.html')

def employers(request):
    try:
        if request.session['admin']:
            emp=Recruiter.objects.all()
            return render(request,'employers.html',{'emp':emp})
    except:
        return render(request,'login.html')

def addnews(request):
    newstext=request.POST['newstext']
    newsdate=date.today()
    nw=News(newstext=newstext,newsdate=newsdate)
    nw.save()
    return redirect('adminhome')

def deletenews(request,id):
    obj=News.objects.get(id=id)
    obj.delete()
    return redirect('adminhome')

def edit_news(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    obj = News.objects.get(id=id)
    if request.method == 'POST':
        n = request.POST['newstext']
        obj.newstext=n
        obj.save()
        alert = True
        return render(request, 'edit_news.html', {'alert': alert})
    return render(request, 'edit_news.html', {'obj': obj})

def delete_emp(request,id):
    obj = Recruiter.objects.get(cpemailaddress=id)
    obj.delete()
    log = Login.objects.get(userid=id)
    log.delete()
    return redirect('employers')

def delete_enquiry(request,id):
    obj = Enquiry.objects.get(emailaddress=id)
    obj.delete()
    return redirect('enquiries')


def delete_js(request,id):
    obj1 = JobSeeker.objects.get(emailaddress=id)
    obj1.delete()
    log=Login.objects.get(userid=id)
    log.delete()
    return redirect('jobseekers')





