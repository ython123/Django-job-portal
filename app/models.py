
from email.policy import default
import numbers
from random import Random, random

from django.db import models


# Create your models here.

# Master Table 

class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.CharField(max_length=250,default="True")
    is_verified = models.CharField(max_length=250,default="False")
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

    
    
# Candidate Table 

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    min_salary = models.CharField(max_length=50 ,default="")
    max_salary = models.CharField(max_length=50,default="") 
    job_type = models.CharField(max_length=150)
    job_category = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    highestedu = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    shift = models.CharField(max_length=150)
    jobdescription = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to="app/img/candidate") 

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

# Company table

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    comapany_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50,default="")
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    website = models.CharField(max_length=150 ,default="")
    description = models.CharField(max_length=700 ,default="")
    logo_pic = models.ImageField(upload_to="app/img/company")

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


# Jobdetails table

class Jobdetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=300)
    companyname = models.CharField(max_length=300)
    companyaddress = models.CharField(max_length=300)
    jobdescription = models.TextField(max_length=700)
    qualification = models.CharField(max_length=300)
    resposibilities = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    companywebsite = models.CharField(max_length=300)
    companyemail = models.CharField(max_length=300)
    companycontact = models.CharField(max_length=300)
    salarypackage = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    job_type = models.CharField(max_length=150,default="")
    comdetaile = models.CharField(max_length=700,default="")


 
    logo = models.ImageField(upload_to="app/img/jobpost",default="")

   



# Applyjob Table

class Applyjob(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job = models.ForeignKey(Jobdetails,on_delete=models.CASCADE)
    education = models.CharField(max_length=300)
    experience = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    min_salary = models.CharField(max_length=250)
    max_salary = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
   
    resume = models.FileField(upload_to="app/resume")




# Get into touch module

class Gettouch(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=1500)
    