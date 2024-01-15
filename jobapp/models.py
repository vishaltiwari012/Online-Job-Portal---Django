from django.db import models

# Create your models here.
class JobSeeker(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50,primary_key=True)
    dob=models.CharField(max_length=20)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    keyskills=models.TextField()
    image=models.FileField(null=True)
    regdate=models.CharField(max_length=20)

class Login(models.Model):
    userid=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=50)


class Recruiter(models.Model):
    firm_name=models.CharField(max_length=100)
    firm_address=models.TextField()
    cpname=models.CharField(max_length=50)
    cpcontactno=models.CharField(max_length=15)
    cpemailaddress=models.EmailField(max_length=50,primary_key=True)
    aadharno=models.CharField(max_length=12)
    panno=models.CharField(max_length=10)
    gstno=models.CharField(max_length=15)
    photo = models.FileField(null=True)
    regdate=models.CharField(max_length=20)


class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    enquirytext=models.TextField()
    posteddate=models.CharField(max_length=30)

class Jobs(models.Model):
    employer=models.ForeignKey(Recruiter,on_delete=models.CASCADE,null=True)
    firmname=models.CharField(max_length=100)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    jobtitle=models.CharField(max_length=100)
    img=models.FileField(null=True)
    jobtype=models.CharField(max_length=50)
    jobdesc=models.TextField()
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    salarypa=models.IntegerField()
    skills=models.CharField(max_length=100,null=True)
    posteddate=models.CharField(max_length=30)
    emailaddress=models.EmailField(max_length=50)

class Apply(models.Model):
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    student=models.ForeignKey(JobSeeker,on_delete=models.CASCADE)
    empemailaddress=models.EmailField(max_length=50,null=True)
    resume=models.FileField(null=True)
    applydate=models.DateField()

class News(models.Model):
    newstext=models.TextField()
    newsdate=models.CharField(max_length=20)

