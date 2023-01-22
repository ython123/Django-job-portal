from email import message
from email.mime import image
from importlib.metadata import requires
from os import stat
from pyexpat.errors import messages
import re
from smtplib import SMTP_SSL
from sre_parse import State
from tracemalloc import start
from urllib import request
from winreg import REG_RESOURCE_REQUIREMENTS_LIST
from wsgiref.handlers import read_environ
from xml.sax.xmlreader import Locator
from xmlrpc.server import resolve_dotted_attribute
from django.db import reset_queries
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from pkg_resources import ResolutionError
from . models import *
from random import randint
from django.core.paginator import Paginator 
# Create your views here.


# Index Page Means Home Page Show View

def IndexPage1(request):
    jobpost_all = Jobdetails.objects.all()
    
           
    jobkey = request.POST.get('jobkey')
    state = request.POST.get('state')
    jobserchtype = request.POST.get('jobserchtype')

    
    if jobkey!='' and jobkey is not None or state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( jobname__icontains = jobkey , location__icontains = state )

    if jobkey!='' and jobkey is not None and state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( jobname__icontains = jobkey , location__icontains = state )
    
    
    if jobserchtype!='' and jobserchtype is not None or state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( job_type__icontains = jobserchtype , location__icontains = state )
   
    if jobserchtype!='' and jobserchtype is not None and state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( job_type__icontains = jobserchtype , location__icontains = state )
   
   
   # Pagination logic definition
   
    page = Paginator(jobpost_all,10)
    page_number = request.GET.get('page')
    finaljobdata = page.get_page(page_number)
    totalpage = finaljobdata.paginator.num_pages

    return render(request,"app/index1.html",{'all_job':finaljobdata,'totalpage':[n+1 for n in range(totalpage)]}) 












    



#def IndexPage2(request):
 #   return render(request,"app/index2.html")


# Signup Page show View

def SignupPage(request):
    return render(request,"app/signup.html")


# Register user Page View 

def RegisterUser(request):

    # Candidate Register process

    if request.POST['role'] == "Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # check user is already are available in your website .

        user = UserMaster.objects.filter( email = email )

        # Check Email is Already avaliable in your website .

        # Server Side Validation 
        if user:
            sms = "User Already exist"
            return render(request,"app/signup.html",{'msg':sms})
        
        # Password and Confirm Password match proces

        else:
            if password == cpassword:

                otp = randint(100000,999999)
                newuser = UserMaster.objects.create( role = role , email = email , password = password , otp = otp)
                newcand = Candidate.objects.create( user_id = newuser , firstname = fname , lastname = lname)
                return render(request,"app/otpverify.html",{'email':email})
                # After Candidate Register render the page for otpverify page

                return render(request,"app/otpverify.html")
            else:
                sms = "Password not match ! "
                return render(request,"app/signup.html",{'msg':sms})
    else:

        
         # Company Register process

        if request.POST['role'] == "Company":
            role = request.POST['role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']

            # check user is already are available in your website .

            user = UserMaster.objects.filter( email = email )

            # Check Email is Already avaliable in your website .

            # Server Side Validation 
            if user:
                sms = "User Already exist"
                return render(request,"app/signup.html",{'msg':sms})
            
            # Password and Confirm Password match proces

            else:
                if password == cpassword:

                    otp = randint(100000,999999)
                    newuser = UserMaster.objects.create( role = role , email = email , password = password , otp = otp)
                    newcand = Company.objects.create( user_id = newuser , firstname = fname , lastname = lname)
                    return render(request,"app/otpverify.html",{'email':email})
                    # After Company Register render the page for otpverify page

                    return render(request,"app/otpverify.html")
                else:
                    sms = "Password not match ! "
                    return render(request,"app/signup.html",{'msg':sms})


# Otpverify Page Render process

def OtpVerifyPage(request):
    return render(request,"app/otpverify.html")



# Otp verification View process

def OtpverificationView(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
  

    # Now Check email is on your database are in or not

    user = UserMaster.objects.get( email = email)

    # If User Are avlaible in your website then chek otp in your database 
    if user:
        # check Otp in your database
        

        if user.otp == otp:
           
            sms = "OTP Verification Successfully ."
            return render(request,"app/login.html",{'msg':sms})
        else:
           
            sms = "OTP Failled"
            return render(request,"app/otpverify.html",{'msg':sms})
    else:
        return render(request,"app/signup.html")


# Login in page show render View

def LoginPage(request):
    return render(request,"app/login.html")

# Login Register page View

def LoginRegister(request):

    # check register user is Candidate or not

    if request.POST['role'] == "Candidate":

        email = request.POST['email']
        password = request.POST['password']

        # Check in database user are available or not 

        user = UserMaster.objects.get( email=email )

        # whenever are user available in your database then check 
        if user:
            if user.password == password and user.role == "Candidate":
                can = Candidate.objects.get( user_id = user )

                # Create Session 

                request.session['role'] = user.role
                request.session['id'] = user.id
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password

                return redirect('indexpage2')
            else:
                sms = "Password incorrect"
                return render(request,"app/login.html",{'msg':sms})
        else:
            sms = "User Does not exist"
            return render(request,"app/login.html",{'msg':sms})

    else:


        # Company Login register process
        if request.POST['role'] == "Company":

            email = request.POST['email']
            password = request.POST['password']

        # Check in database user are available or not 

            user = UserMaster.objects.get( email = email )

        # whenever are user available in your database then check 
            if user:
                if user.password == password and user.role == "Company":
                    cam = Company.objects.get( user_id = user )

                    # Create Session 

                    request.session['role'] = user.role
                    request.session['id'] = user.id
                    request.session['firstname'] = cam.firstname
                    request.session['lastname'] = cam.lastname
                    request.session['email'] = user.email
                    request.session['password'] = user.password

                    return redirect('companyIndexpage')
                else:
                    sms = "Password incorrect"
                    return render(request,"app/login.html",{'msg':sms})
            else:

                sms = "User Does not exist"
                return render(request,"app/login.html",{'msg':sms})


# Profile page Render definition
# Pk are used fro transefer the data  from profile page 
def ProfilePage(request,pk):

    user = UserMaster.objects.get( pk = pk)
    can = Candidate.objects.get(user_id = user)
    return render(request,"app/profile.html",{'user':user ,'can':can})



# Update Profil Page Data process 

def UpdatProfile(request,pk):
    # First get the data from UserMaster table 
    user = UserMaster.objects.get(pk=pk)

    # check role 

    if user.role == "Candidate":
        can = Candidate.objects.get(user_id = user)

        can.country = request.POST['country'] # First Country is belong database field and second Country is belongs to html input name 
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.job_type = request.POST['jobtype']
        can.job_category = request.POST['category']
        can.highestedu = request.POST['education']
        can.experience = request.POST['exprience']
        can.website = request.POST['website']
        can.shift = request.POST['shift']
        can.jobdescription = request.POST['jobdescription']
        can.min_salary = request.POST['minsalary']
        can.max_salary = request.POST['maxsalary']
        can.contact = request.POST['contact']
        can.gender = request.POST['gender']
        can.profile_pic = request.FILES['image']
        can.save()

        url = f'/profilepage/{pk}' # formatting url 
        return redirect(url)



# Apply Page render code 

def ApplyPage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user:
        can = Candidate.objects.get(user_id = user)
        job = Jobdetails.objects.get(id=pk)
        return render(request,"app/apply.html",{'user':user,'can':can,'job':job})

# Candidate profile page



def CandidateprofilePage(request):
        user = UserMaster.objects.all()
        can = Candidate.objects.all()
        job = Jobdetails.objects.all()
        return render(request,"app/candidates-profile.html",{'user':user,'can':can,'job':job})


# Apply list page definition

def ApplyjobView(request,pk):

    user = request.session['id']

    if user:

        can = Candidate.objects.get(user_id = user)
        job = Jobdetails.objects.get(id=pk)

        education = request.POST['education']
        experience = request.POST['experience']
        website = request.POST['website']
        gender = request.POST['gender']
        resume = request.FILES['resume']
        min_salary = request.POST['min_salary']
        max_salary = request.POST['max_salary']


        applyjob = Applyjob.objects.create( candidate = can , job = job , education = education , website = website , 
                                            experience = experience , gender = gender , min_salary = min_salary ,
                                            max_salary = max_salary , resume = resume )
        sms = "Applied job successfully . "
        return render(request,"app/apply.html",{'msg':sms}) 


#################################### Company Side ##############################################

# CompanyIndex oage render 

def CompanyindexPage(request):
    applyjob_list = Applyjob.objects.all()
    return render(request,"app/company/index.html",{'applyjob_list':applyjob_list})



# CompanyPrifile oage render 

def Companyprofile(request):
    return render(request,"app/company/profile.html")



# Company Profile Page render 

def CompanayprofilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id = user)
    return render(request,"app/company/profile.html",{'user': user,'comp':comp})


            
# Update Company 

# Company Update Profile Page 
def UpdatecompanyProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)


    if user.role == "Company":
        comp = Company.objects.get(user_id = user)
        comp.firstname = request.POST['firstname']
        comp.lastname = request.POST['lastname']
        comp.comapany_name  = request.POST['company']
        comp.state  = request.POST['state']
        comp.city  = request.POST['city']
        comp.country =request.POST['country']
        comp.contact  = request.POST['contact']
        comp.address  = request.POST['address']
        comp.description = request.POST['description']
        comp.website = request.POST['website'] 
        comp.logo_pic = request.FILES['image']

        comp.save()

        url = f'/companyprofilepage/{pk}'
        return redirect(url)


# Post Job page render process


# 
def Jobpostpage(request):
    return render(request,"app/company/jobpost.html")


def Tablepage(request):
    return render(request,"app/company/tables.html")

# Jodetail Post 

def JobDetailSubmit(request,pk):
    # Get user  ! which user are stord in company detail
    user = UserMaster.objects.get(pk=pk  ) 
   

    # check the  first user role is Company then post the job  

    if user.role == "Company":
        comp = Company.objects.get( user_id = user )

        cjobname = request.POST['cjobname']
        cname = request.POST['cname']
        caddress = request.POST['caddress']
        ccontact = request.POST['ccontact']
        cwebsite = request.POST['cwebsite']
        companyemail = request.POST['cemail'] 
        cjobdescription = request.POST['cjobdescription']
        cqualification = request.POST['cqualification']
        cresponsiblities = request.POST['cresponsibilities']
        clocation = request.POST['clocation']
        csalarypackage = request.POST['csalarypackage']
        cexeperience = request.POST['cexperience']
        cjobtype = request.POST['jobtype']
        ccomdetaile = request.POST['comdetaile']
       
        logo = request.FILES['cimage']

        # query for Insert data 

        insertjob = Jobdetails.objects.create( company_id = comp , jobname = cjobname , companyname = cname ,
        companyaddress = caddress , jobdescription = cjobdescription , qualification = cqualification ,
        resposibilities =  cresponsiblities ,  location = clocation , companywebsite = cwebsite ,
        companyemail =  companyemail ,   companycontact = ccontact , salarypackage = csalarypackage ,
        experience = cexeperience ,job_type = cjobtype, logo = logo  ,   comdetaile  = ccomdetaile )

        sms = " Job post Successfully "

        return render(request,"app/company/jobpost.html",{'msg':sms})



        
# Job post list page render definition

def JobpostList(request):
    # fetch ALL job post lis in job post list data
    jobpost_all = Jobdetails.objects.all()
    return render(request,"app/company/jobpostlist.html",{'all_job':jobpost_all})


# Company job post list send page from candidate

# Job post list page render definition

def CandiatejobposList(request):
    # fetch ALL job post lis in job post list data
    jobpost_all = Jobdetails.objects.all()
    
           
    jobkey = request.POST.get('jobkey')
    state = request.POST.get('state')
    jobserchtype = request.POST.get('jobserchtype')

    
    if jobkey!='' and jobkey is not None or state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( jobname__icontains = jobkey , location__icontains = state )

    if jobkey!='' and jobkey is not None and state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( jobname__icontains = jobkey , location__icontains = state )
    
    
    if jobserchtype!='' and jobserchtype is not None or state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( job_type__icontains = jobserchtype , location__icontains = state )
   
    if jobserchtype!='' and jobserchtype is not None and state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( job_type__icontains = jobserchtype , location__icontains = state )
   
   
   # Pagination logic definition
   
    page = Paginator(jobpost_all,10)
    page_number = request.GET.get('page')
    finaljobdata = page.get_page(page_number)
    totalpage = finaljobdata.paginator.num_pages

    return render(request,"app/job-list.html",{'all_job':finaljobdata,'totalpage':[n+1 for n in range(totalpage)]}) 
  




# Company job post list send page from candidate



def IndexPage2(request): 
    jobpost_all = Jobdetails.objects.all()
    
           
    jobkey = request.POST.get('jobkey')
    state = request.POST.get('state')
    jobserchtype = request.POST.get('jobserchtype')

    
    if jobkey!='' and jobkey is not None or state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( jobname__icontains = jobkey , location__icontains = state )

    if jobkey!='' and jobkey is not None and state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( jobname__icontains = jobkey , location__icontains = state )
    
    
    if jobserchtype!='' and jobserchtype is not None or state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( job_type__icontains = jobserchtype , location__icontains = state )
   
    if jobserchtype!='' and jobserchtype is not None and state!='' and state is not None:
        jobpost_all = Jobdetails.objects.filter( job_type__icontains = jobserchtype , location__icontains = state )
   
   
    
   # Pagination logic definition
   
    page = Paginator(jobpost_all,10)
    page_number = request.GET.get('page')
    finaljobdata = page.get_page(page_number)
    totalpage = finaljobdata.paginator.num_pages

    return render(request,"app/index2.html",{'all_job':finaljobdata,'totalpage':[n+1 for n in range(totalpage)]}) 
  
    




    






        
    




# Job detail page
# job  detail redner for job detail.html
def JobdetailPage(request):
    jobpost_all = Jobdetails.objects.all()
    return render(request,"app/job-details.html",{'all_job':jobpost_all})







# Applyjob list 

def ApplyjoblList(request):
    applyjob_list = Applyjob.objects.all()
    return render(request,"app/company/applyjoblist.html",{'applyjob_list':applyjob_list})




#   Company about  page

def CompanyaboutPage(request):
    return render(request,"app/company/about.html")


#   Company Carrier  page

def CompanycarrierPage(request):
    return render(request,"app/company/carrier.html")

# Company Contact page 

def CompanycontactPage(request):
    return render(request,"app/company/contact.html")

# Company gettoucch page 

def CompanygettouchData(request):

    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    user = Gettouch.objects.create( name = name , email = email , subject = subject , message = message )

    if user.name == "" and user.email == "" and user.subject == "" and user.message=="":
        sms = "Send your Request Failled. "
        return render(request,"app/company/contact.html",{'red':sms})
    else:
        sms = "Send your request Successfully ! And You will be given your response soon ."
        return render(request,"app/company/contact.html",{'green':sms})



# Company Support page

def CompanysupportPage(request):
    return render(request,"app/company/support.html")

# Company Privacy policy page 

def CompanyprivacypolicyPage(request):
    return render(request,"app/company/privacy-policy.html")





###################################### log OUT Definition ##################################33333

# Company Logout definition

def CompanyLogOut(request):
    del request.session['email']
    del request.session['password']
    return redirect('indexpage1')


# Candidate Logout definition

def CandidatelogOut(request):
    del request.session['email']
    del request.session['password']
    return redirect('indexpage1')





        




############################################## Admin Page ###############################################


def AdminSite(request):
    return render(request,"app/admin/login.html")



# Admin login process

def AdminLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":
        request.session['username'] = username
        request.session['password'] = password

        return redirect('adminhomepage')
    else:

        sms = "User name and Password not match ."
        return render(request,"app/admin/login.html",{'msg':sms})


# Admin home page

def AdminhomePage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"app/admin/index.html")
    else:
        return redirect('adminpage')



# Admin Logout definition




# Admin user list 

def AdminuserList(request):
    all_user = UserMaster.objects.filter( role = "Candidate")
    return render(request,"app/admin/userlist.html",{'userlist':all_user})

# Admin Company list 

def AdmincompanyList(request):
    all_company = UserMaster.objects.filter(role = "Company")
    return render(request,"app/admin/companylist.html",{'companylist':all_company})


# Admin user delete operation

def AdminUserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')



# Update Is_verified field false to true

def AdminUpdateverified(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request,"app/admin/verify.html",{'company':company})


# Company update verify code 

def CompanyverifyPage(request,pk):
    company = UserMaster.objects.get(pk=pk)

    if company: 
        company.is_veryfied = request.POST['verify']
        company.save()
        return redirect('companylist')


# Admi Company delete operation

def AdmincompanyDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('companylist')
    

        
        
        
        
        


# Contact page View
def Contact(request):
    return render(request,"app/contact.html")



# Imnsert get touc data in contact .html 

def Gettouchdata(request):

    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    user = Gettouch.objects.create( name = name , email = email , subject = subject , message = message )

    if user.name == "" and user.email == "" and user.subject == "" and user.message=="":
        sms = "Send your Request Failled      ."
        return render(request,"app/contact.html",{'red':sms})
    else:
        sms = "Send your request Successfully ! And You will be given your response soon"
        return render(request,"app/contact.html",{'green':sms})



        

# Aboutpage view

def AboutPage(request):
    return render(request,"app/about.html")



# Job detail2 page

def Jobdetail2Page(request):
    return render(request,"app/job-details-2.html")

# hob grid 
def JobgridPage(request):
    return render(request,"app/job-grid.html")


####################### pages ####################

# servicess page
def ServicesPage(request):
    return render(request,"app/services.html")

# Team pages 

def TeamPage(request):
    return render(request,"app/team.html")

# faqpage

def FaqPage(request):
    return render(request,"app/faq.html")

# Pricingplan page

def PricingplanPage(request):
    return render(request,"app/pricing.html")

####################3 candidate pages #################################3

# Candidate listing page

def CandidateListing(request):
    return render(request,"app/candidates-listing.html")


# REsume render page     
def Creatreaume(request):
    return render(request,"app/create-resume.html")

####################Employer #############################

def Employelist(request):
    return render(request,"app/employers-list.html")

def Companydetail(request):
    return render(request,"app/company-detail.html")


# forget passworf page
def RecoveryPasssword(request):
    return render(request,"app/recovery_passward.html")

############### component #####################
# Component page

def Componentpage(request):
    return render(request,"app/components.html")

########################3 provacy policy ################33333

def PrivacypolicyPage(request):
    return render(request,"app/privacy-policy.html")

######################## Carier page #####################3


def CarrierPage(request):
    return render(request,"app/carrier.html")


###################3333333 Support page ##############33


def SupportPage(request):
    return render(request,"app/support.html")







def SerchoptionPage(request):
    return render(request,"app/serch.html")