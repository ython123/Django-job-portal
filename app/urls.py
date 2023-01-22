
from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static
from pydoc import visiblename
from unicodedata import name
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.IndexPage1,name="indexpage1"),
    
    path("indexpage2/",views.IndexPage2,name="indexpage2"),
    path("signuppage/",views.SignupPage,name="signuppage"),
    path("register/",views.RegisterUser,name="register"),
    path("otppage/",views.OtpVerifyPage,name="otppage"),
    path("otpverificationypage/",views.OtpverificationView,name="otpverificationpage"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("login/",views.LoginRegister,name="login"),
    path("profilepage/<int:pk>",views.ProfilePage,name="profilepage"),
    path("updateprofile/<int:pk>",views.UpdatProfile,name="updateprofile"),
    path("candidatejobpostlist/",views.CandiatejobposList,name="candidatejobpostlist"),
    path("applypage/<int:pk>",views.ApplyPage,name="applypage"),
    path("applyjob/<int:pk>",views.ApplyjobView,name = "applyjob"),

    path("candidateprofilepage/",views.CandidateprofilePage,name="candidateprofilepage"),

    ################################## Candidate Logout url ###########################

    path("candidatelogout/",views.CandidatelogOut,name="candidatelogout"),

    


    #################### Company side url ###################################

    path("companyIndexpage/",views.CompanyindexPage,name="companyIndexpage"),
    path("companyprofile/",views.Companyprofile,name="companyprofile"),
    path("companyprofilepage/<int:pk>",views.CompanayprofilePage,name="companyprofilepage"),
    path("updatecompanyprofilepage/<int:pk>",views.UpdatecompanyProfile,name="updatecompanyprofilepage"),
    
    path("postpage/",views.Jobpostpage,name="postpage"),
    path("jobpost/<int:pk>",views.JobDetailSubmit,name="jobpost"),
    path("jobpostlist/",views.JobpostList,name="jobpostlist"),
    path("tablepage/",views.Tablepage,name="tablepage"),

    #################### Company Log out url #########################
    path("companylogoutpage/",views.CompanyLogOut,name="companylogout"),
    #####################################################################
    path("applyjoblist/",views.ApplyjoblList,name="applyjoblist"),

#########################3 Company about page ##################
  path("companyaboutpage/",views.CompanyaboutPage,name="companyaboutpage"),
  ########################### company carrier page #############
  path("companycarrierpage/",views.CompanycarrierPage,name="companycarrierpage"),

  ################################ company contact page ##############

  path("companycontactpage/",views.CompanycontactPage,name="companycontactpage"),

  ###############################3 company get touch url ############

  path("companygettouchdata",views.CompanygettouchData,name="companygettouchdata"),

  ############################33 Company support page #######

  path("companysupportpage/",views.CompanysupportPage,name="companysupportpage"),

  ############################3 company privacy policy page ##############

  path("companyprivacypolicypage/",views.CompanyprivacypolicyPage,name="companyprivacypolicypage"),

     




    ######################### Admin Site url #######################################3


    path("adminpage/",views.AdminSite,name="adminpage"),
    path("adminloginpage/",views.AdminLogin,name="adminloginpage"),
    path("adminhomepage/",views.AdminhomePage,name="adminhomepage"),
    
    path("userlist/",views.AdminuserList,name="userlist"),
    path("companylist/",views.AdmincompanyList,name="companylist"),
    path("userdeletelist/<int:pk>",views.AdminUserDelete,name="userdeletelist"),
    path("adminupdateverify/<int:pk>",views.AdminUpdateverified,name="adminupdateverify"),
    path("companyverifypage/<int:pk>",views.CompanyverifyPage,name="companyverifypage"),
    path("companydeletelist/<int:pk>",views.AdmincompanyDelete,name="companydeletelist"),




  ###########################3 privcy policy in dream job successlif ############3

    path("privacypolicypage/",views.PrivacypolicyPage,name="privacypolicypage"),

    #########################33 carrier page url #######################3

    path("carrierpage/",views.CarrierPage,name="carrierpage"),


    ########################3 Support url #####################

    path("supportpage/",views.SupportPage,name="supportpage"),
    

    ######################################### contact code ############################

    path("contactpage/",views.Contact,name="contactpage"),
    path("gettouchdata/",views.Gettouchdata,name="gettouchdata"),

    ################################### about code ######################

   path("aboutpage/",views.AboutPage,name="aboutpage"),


   ###############################3 job detail page #################

   path("jobdetailpage/",views.JobdetailPage,name="jobdetailpage"),

   ###############################3 job detail2 page #################

   path("jobdetail2page/",views.Jobdetail2Page,name="jobdetail2page"),

    ###############################3 job grid page #################

   path("jobgridpage/",views.JobgridPage,name="jobgridpage"),


 ##########################pages ################################33

 path("servicespages/",views.ServicesPage,name="servicespage"),
 path("teampage/",views.TeamPage,name="teampages"),
 path("faqpage/",views.FaqPage,name="faqpage"),
 path("pricingpage/",views.PricingplanPage,name="pricingpage"),
 path("candidatelistingpage/",views.CandidateListing,name="candidatelistingpage"),


 path("createresume/",views.Creatreaume,name="createresume"),

###############################33 employe url ####################3

 path("employelistpage/",views.Employelist,name="employerlistpage"),
 path("companypage/",views.Companydetail,name="companypage"),

  #######################forget password url #############33

  
 path("recoverypasswordpage/",views.RecoveryPasssword,name="recoverypasswordpage"),

 ####################component############################3

 path("componentpage/",views.Componentpage,name="componentpage"),


path("serchoptionpage/",views.SerchoptionPage,name="serchoptionpage"),




]  

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
















