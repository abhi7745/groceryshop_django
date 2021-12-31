from django.db.models.aggregates import Count
from django.http.response import JsonResponse # for json respone (Ajax)
from django.template.loader import render_to_string # for coverting template data and render to it(Ajax)
from django.db.models import Min,Max # for product data filtering by min,max values

from django.shortcuts import render, redirect

# ///////// my model.py ///////////////
from homeapp.models import *

# /////// for login purpose //////////////
from django.contrib.auth.decorators import login_required

# importing django login athentications
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth import login as log,logout,authenticate

# importing password encryptor
from django.contrib.auth.hashers import make_password, check_password 

# from django.contrib.auth.models import *

from admin_sellerapp.models import * #importing all admin_sellerapp models

from productsapp.models import * #importing all productsapp  models

# Create your views here.

# //////////////// homeapp view start ////////////////
# homepage
def homepage(request):

    shoplist=seller_reg.objects.all() # getting seller_reg table all data

    if request.user.is_authenticated:
        print(request.user,'GO VAAAAAAA') # request.user holds the user logged in value (eg: jon )
        # log_data=request.user
        profile_authuser=User.objects.filter(username__contains=request.user)
        for usa in profile_authuser:
            print(usa.id,'already logged in')

        # admin login condition
        if(usa.first_name=='admin'):
            print('success aaaaaaaaaaaaaaaaaaaaaaaaa')
            print('admin is logged in')
            return render(request,'adminpanel/dashboard.html',{})

        # seller login condition
        elif(usa.first_name=='seller'):
            print('success sssssssssssssssssssssssss')
            print('seller is logged in')
            return render(request,'sellerpanel/dashboard.html',{})

        # user login condition
        elif(usa.first_name=='user'):
            print('success uuuuuuuuuuuuuuuuuuuuuuuuu')
            print('user is logged in')
            
            return render(request,'userpanel/loggedhome/shoplistbody.html',{'sample':usa,'shoplist':shoplist})
        else:
            print('Totally Invalid user')
            # return render(request,'userpanel/login.html',{'checker':'Invalid Email & Password already'})
            return redirect(logoutpage)

    else:
        return render(request,'userpanel/shoplistbody.html',{'shoplist':shoplist})

    # return render(request,'userpanel/shoplistbody.html',{'shoplist':shoplist})
    
# Homepage sub functionality
# Ajax loader function for shop lists filtering purpose
def shoplistfilter(request): # For ajax loading purpose 
    # colors=request.GET.getlist('colors[]')
    # for option values
    cat=request.GET.getlist('Categories[]')

    # print(colors,'that value')
    print(cat,'that value cat')

    allpro=seller_reg.objects.all()
    # print(allpro,'checker')

    # allProducts=product.filter(pro_price__gte=minPrice)
    # allProducts=product.filter(pro_price__lte=maxPrice)

    if len(cat)>0:
        print('len ok')
        allpro=allpro.filter(s_pincode__in=cat)
        print(allpro,'allpro')

    tem=render_to_string('userpanel/ajax/shoplistbody.html',{'shoplist':allpro})
    # print(tem,'tem')
    
    return JsonResponse({'data':tem})



#  Ajax loader function for products lists filtering purpose
def productsfilter(request): # For ajax loading purpose
    # for range values
    minPrice=request.GET['minPrice']
    maxPrice=request.GET['maxPrice']

    shopid=request.GET['shopid'] #shopid is for filtering which shop is this 

    cat=request.GET.getlist('Categories[]') #
    print(type(cat),cat,'this is a cat')    #

    # print(minPrice,'that range min')
    # print(maxPrice,'that range max')
    # print(shopid,'that shopid')
    # print(type(shopid),'that shopid')

    check=product.objects.all()
    print(check.count(),'product database count')

    whichshopnow=product.objects.filter(seller_id_id=int(shopid))

    ######################################

    for x in whichshopnow:
        print(x.pro_category,'i am mmmmmmmmmmmmmmmm')
        print(type(x.pro_category),'heyyyyyyyyyyy')
    

    mycat=''.join(cat)
    print(type(mycat),mycat,'mycat')

    # Almost ready
    if whichshopnow.filter(pro_category__in=cat):
        print('true')
    else:
        print('false')
    catpro=whichshopnow.filter(pro_category__in=cat)
    print(catpro,'catpro')

    #################################



    print(whichshopnow.count(),'whichshopnow')

    # if len(minPrice)>0 and len(maxPrice)>0 :
    if len(whichshopnow)>0:
        print('len ok')

    allpro=whichshopnow.filter(pro_price__gte=minPrice).order_by('pro_price')
    allpro=whichshopnow.filter(pro_price__lte=maxPrice).order_by('pro_price')
        # print(allpro,'tester')
    noproducts=allpro.count() # no products is in that price
    print(noproducts,'noproductss')

    # if len(cat)>0:
    #     print('len cat ok')
    # catpro=whichshopnow.filter(pro_category__contains=cat)
    # print(catpro,'catpro')

    tem=render_to_string('userpanel/ajax/shopproducts.html',{'seller_pro_list':allpro,'noproducts':noproducts})
    return JsonResponse({'data':tem})

# User Registration (Home Page - signup)
def userreg(request):
    if request.method=='POST':
            name=request.POST.get('name')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            pincode=request.POST.get('pincode')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_psd=request.POST.get('confirm_psd')
            
            print(type(password),'first',password)
            print(type(confirm_psd),'last',confirm_psd)
            # print(name)
            # print(address)
            # print(phone)
            # print(pincode)
            # print(email)
            # print(password)

            # namelen=len(name)
            # email_len=len(email)
            # print('name',namelen)
            # print('email',email_len)
            

            if(name=='' or email== '' or password==''):
                print('No value')
                return render(request,'userpanel/signup.html',{'checknull':'Please enter valid info...'})

            elif(len(name)<3):
                print('Name Length missing')
                return render(request,'userpanel/signup.html',{'checknull':'Name length missing...'})
                
            elif(len(phone)<10) or (len(phone)>=11):
                print('Invalid phone number')
                return render(request,'userpanel/signup.html',{'checknull':'Invalid phone number'})

            elif(len(pincode)<6) or (len(pincode)>=7):
                print('Invalid pincode')
                return render(request,'userpanel/signup.html',{'checknull':'Invalid pincode'})

            elif(not password==confirm_psd):
                print('Password Missmatch')
                return render(request,'userpanel/signup.html',{'checknull':'password Missmatch'})
                    

            else:
                if(not email.endswith('@gmail.com')):
                    print('Email Length missing')
                    return render(request,'userpanel/signup.html',{'checknull':'Email length missing...'})

                elif User.objects.filter(username=email).exists():
                    print('User already exist View')
                    return render(request,'userpanel/signup.html',{'checkuser':'User already exist...'})
                else:
                    #making password encryption for login purpose(becz django weak password is not allowed in authentication)
                    passEncrypted = make_password(password) 

                    # saving email & password in auth_user table (Like Login table)
                    ulog=User()
                    ulog.username=email
                    ulog.password=passEncrypted # saved password in encrypted format
                    ulog.first_name='user'
                    ulog.save()
                    print('auth_user table saved')

                    # saving user data in user_reg table (name,address,phone,pincode)
                    reg=user_reg()
                    reg.user_id=ulog  # assigning user_reg (foriegnkey) <== in auth_user (primarykey) (Get complete table)
                    reg.u_name=name
                    reg.u_address=address
                    reg.u_phone=phone
                    reg.u_pincode=pincode
                    reg.u_email=email
                    reg.save()
                    print('user_reg table saved')
                    return render(request,'userpanel/login.html',{})

    print('Signup View')
    return render(request,'userpanel/signup.html',{})
        

# Seller Registration (Home Page - SignupVendor)
def sellerreg(request):
    if request.method=='POST':
            sname=request.POST.get('sname')
            shopname=request.POST.get('shopname')
            shopaddress=request.POST.get('shopaddress')
            shoplocation=request.POST.get('shoplocation')

            #imagefields
            coverphoto=request.FILES['coverphoto']# ImageField or FileField - vannal must aayi request.FILES["name of input type="file"]
            profilepicture=request.FILES['profilepicture'] # because request.FILES[""] -illotta files varunnatth.      
            idproof=request.FILES['idproof']# don't use this method : idproof=request.POST.get('image') totally worng xxxxxxxxxxxxxxxxxx

            sphone=request.POST.get('sphone')
            aadhaar=request.POST.get('aadhaar')
            gst=request.POST.get('gst')
            spincode=request.POST.get('spincode')
            state=request.POST.get('state')
            district=request.POST.get('district')
            taluk=request.POST.get('taluk')
            semail=request.POST.get('semail')
            spassword=request.POST.get('spassword')

            # print(sname)
            # print(shopname)
            # print(shopaddress)
            # print(shoplocation)
            # print(coverphoto)
            # print(profilepicture)
            # print(sphone)
            # print(aadhaar)
            # print(idproof)
            # print(gst)
            # print(spincode)
            # print(state)
            # print(district)
            # print(taluk)
            # print(semail)
            # print(spassword)

            # saving email & password in auth_user table (Like Login table)
            S_passEncrypted = make_password(spassword) #making password encryption for login purpose(becz django weak password is not allowed in authentication)

            # auth_User table saving (master table)
            slog=User() #Creating Auth_User table object
            slog.username=semail
            slog.password=S_passEncrypted
            slog.first_name='seller'
            slog.save()
            print('saved slog',slog)

            # approval table saving (child 1)
            # approval_tbl=approval()
            # approval_tbl.seller_id=slog # assigning approval table (foriegnkey) <== in auth_user (primarykey) (Get complete table)
            # approval_tbl.email=semail
            # approval_tbl.sellerstate='Deactive'
            # approval_tbl.save()
            # print('saved approval_tbl',approval_tbl)

            # seller_reg table saving (child 2)
            s_reg=seller_reg() #Creating seller_reg table object
            s_reg.seller_id=slog # assigning seller_reg (foriegnkey) <== in auth_user (primarykey) (Get complete table)
            s_reg.s_fullname=sname
            s_reg.s_shopname=shopname
            s_reg.s_address=shopaddress
            s_reg.s_location=shoplocation
            s_reg.s_coverphoto=coverphoto #imagefield
            s_reg.s_profilepic=profilepicture #imagefield
            s_reg.s_phone=sphone
            s_reg.s_aadhaar=aadhaar
            s_reg.s_idproof=idproof #imagefield
            s_reg.s_gstno=gst
            s_reg.s_pincode=spincode
            s_reg.s_state=state
            s_reg.s_district=district
            s_reg.s_taluk=taluk
            s_reg.s_email=semail

            s_reg.sellerstate='Deactive' #added new field (for approval purpose)
            
            s_reg.save()
            print('saved s_reg',s_reg)
            return render(request,'userpanel/login.html',{})


    return render(request,'userpanel/signupvendor.html',{})

# Login Page (Home Page)
def loginpage(request):
    # if (not request.session.session_key == None):
    #     print('true','hai mone')
    # else:
    #     print('false','hai da')

    shoplist=seller_reg.objects.all() # getting seller_reg table all data
    
    # user already logged in area (case 1)
    if request.user.is_authenticated:
        print(request.user,'GO VAAAAAAA') # request.user holds the user logged in value (eg: jon )
        # log_data=request.user
        profile_authuser=User.objects.filter(username__contains=request.user)
        for usa in profile_authuser:
            print(usa.id,'already logged in')

        # log_data_tbl=User.objects.filter(username__contains=user)
        # for usa in loggedin_id:

        # admin login condition
        if(usa.first_name=='admin'):
            print('success aaaaaaaaaaaaaaaaaaaaaaaaa')
            print('admin is logged in')
            return render(request,'adminpanel/dashboard.html',{})

        # seller login condition
        elif(usa.first_name=='seller'):
            print('success sssssssssssssssssssssssss')
            print('seller is logged in')
            return render(request,'sellerpanel/dashboard.html',{})

        # user login condition
        elif(usa.first_name=='user'):
            print('success uuuuuuuuuuuuuuuuuuuuuuuuu')
            print('user is logged in')
            return render(request,'userpanel/loggedhome/shoplistbody.html',{'sample':usa,'shoplist':shoplist})
        else:
            print('Totally Invalid user')
            # return render(request,'userpanel/login.html',{'checker':'Invalid Email & Password already'})
            return redirect(logoutpage)


        # return render(request,'userpanel/loggedhome/shoplistbody.html',{'sample':loggedin_id})
    else:
        
        # user not logged in area (case 2)
        if request.method=='POST':
            email=request.POST.get('email')
            password=request.POST.get('password')

            print(request.POST.items())
            print(email)
            print(password)

            user =authenticate(request, username=email, password=password)

            # u=User.objects.get(username=email,password=password)

            if user is not None:
                login(request, user) #login is hold uservalue(request&user), and added to django_section database
                # print(u,'this is u')
                print(type(user),user)

                # profile_authuser is a condition for who is logged in and collect her data and pass 'id' to loggedbase.html
                profile_authuser=User.objects.filter(username__contains=email)
                for loggedin_id in profile_authuser:
                    print(loggedin_id.id,'who am I')


                # conditon for  U_S_A login (U-User, S-Seller, A-Admin )
                log_data_tbl=User.objects.filter(username__contains=user)
                for usa in log_data_tbl:

                    # admin login condition
                    if(usa.first_name=='admin'):
                        print('success aaaaaaaaaaaaaaaaaaaaaaaaa')
                        print('admin is logged in')
                        return render(request,'adminpanel/dashboard.html',{})

                    # seller login condition
                    elif(usa.first_name=='seller'):
                        print('success sssssssssssssssssssssssss')
                        print('seller is logged in')
                        return render(request,'sellerpanel/dashboard.html',{})

                    # user login condition
                    elif(usa.first_name=='user'):
                        print('success uuuuuuuuuuuuuuuuuuuuuuuuu')
                        print('user is logged in')
                        return render(request,'userpanel/loggedhome/shoplistbody.html',{'sample':loggedin_id,'shoplist':shoplist})

                    else:
                        print('Totally Invalid user')
                        return render(request,'userpanel/login.html',{'checker':'Invalid Email & Password auth'})
                # conditon for normal Seller login
                # for s in log_data_tbl:
                #     if(s.first_name=='seller'):
                #         print('success ssssssssssssssssssssssss')
                #         print('seller is logged in')
                #     else:
                #         print('not a seller nooooooooooooooooooooo')

                # if(User.objects.filter(first_name__contains='seller')):
                #     print('seller is logged in')

            else:
                print(user)
                print('login failed user') 
                return render(request,'userpanel/login.html',{'checker':'Invalid Email & Password auth'}) 


                # old code area
                        # if User.objects.filter(username=email,password=password).exists():
            #     u=User.objects.get(username=email,password=password)
            #     if u.username==email and u.password==password:

                
            #         user = authenticate(request, username=email, password=password)
            #         if user is not None:
            #             login(request, user)
            #             return render(request,'userpanel/loggedhome/shoplistbody.html',{})
            #         else:
            #             print(user)
            #             print('login failed user')
            #             print(email,'first')
            #             print(password,'second')
            #             return render(request,'userpanel/login.html',{'checker':'Invalid Email & Password auth'}) 
                        


            #         print('login success')
            #         # userdata=user_reg.objects.get(u_id=int(value))
            #         # profile_id=user_reg.objects.filter()

            #         # profile_userdata=user_reg.objects.filter(u_id__icontains=25)

            #         profile_authuser=User.objects.filter(username__contains=email) # getting current user from auth_user table
            #         # sample=user_reg.objects.filter(u_id__contains=25)

            #         # for x in profile_userdata:
            #         #     print(x.u_address)

            #         for y in profile_authuser:
            #             print(y.id)
                        
            #         return render(request,'userpanel/loggedhome/shoplistbody.html',{'sample':y}) 
            #         #sample(dictionary) holds specific login user(auth_user table) and --
            #         # pass user "id" to logged shoplistbody.html in the format(eg: {% url 'userregview_url' sample.id %})
            # else:
            #     print('login failed')
            #     return render(request,'userpanel/login.html',{'checker':'Invalid Email & Password'})    

            
    return render(request,'userpanel/login.html')  

# shop products
# @login_required(login_url='/login')
def productlist(request,pk):
    filterdata=pk #filterdata is for passing id of a specified seller_reg value
    print(pk)
    seller_pro_list=product.objects.filter(seller_id_id=pk)
    print(seller_pro_list)
    

    if request.user.is_authenticated:
        print('auth user')

        profile_authuser=User.objects.filter(username__contains=request.user) #for passing user id for profile view set up
        for usa in profile_authuser:
            print(usa.id,'already logged in')
        return render(request,'userpanel/loggedhome/shopproducts.html',{'sample':usa,'seller_pro_list':seller_pro_list,
        'count':seller_pro_list.count()})

    else:
        # Ajax filter condition for passing the user range values from shopproducts.html file
        minMaxPrice=product.objects.aggregate(Min('pro_price'),Max('pro_price'))
        print(minMaxPrice)

        print('unknown user')
        return render(request,'userpanel/shopproducts.html',{'seller_pro_list':seller_pro_list,
        'count':seller_pro_list.count(),'minMaxPrice':minMaxPrice,'filterdata':filterdata})
        
        


    
    # return render(request,'userpanel/shopproducts.html',{'seller_pro_list':seller_pro_list})
# checkout
def checkoutpage(request):
    return render(request,'userpanel/checkout.html',{})
# paymentpage
def paymentpage(request):
    return render(request,'userpanel/payment.html')
# COD
def cod(request):
    return render(request,'userpanel/cod.html')
# token page
def tokenpage(request):
    return render(request,'userpanel/tokenpage.html')

# net banking
def netbanking(request):
    if request.method=='POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        securitycode= request.POST.get('securitycode')
        expiration=request.POST.get('expiration')

        print(name)
        print(number)
        print(securitycode)
        print(expiration)

    return render(request,'userpanel/netbanking.html')
# about
def aboutpage(request):
    return render(request,'userpanel/about.html')

# contact
def contactuspage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')

            
        print(name)
        print(subject)
        print(email)
        print(message)
    return render(request,'userpanel/contact.html')



# //////////////// homeapp view end ////////////////


#////////////////// custom views - for a special purpose start ///////////////

# Individual user data viewing purpose
def userregview(request,value):  # Viewing purpose (fetching user_reg db and auth_user(login) db values)
    profile=user_reg.objects.get(user_id_id=int(value))
    profile_login_tbl=User.objects.get(id=int(value))
    print(profile,'my success')
    print(profile_login_tbl,'my sucess-2')

    return render(request,'userpanel/loggedhome/edituserprofile.html',{'profile':profile,'profile_login_tbl':profile_login_tbl})

# Individual user data updation purpose
def userregupdation(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        pincode=request.POST.get('pincode')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user_id=request.POST.get('db_id') #db_id is a name of html tag(hidden input_text)
        print(user_id)

        # auth_user table field (finding specific user- using by 'id'(primary-key) )
        db_user=User.objects.get(id=int(user_id)) 
        print(db_user)

        # Re-assigning and saving data into specific auth_user table field (With the help of object(db_user))
        db_user.username=email
        db_user.password=password
        db_user.save()

         # user_reg table field (finding specific user- using by 'user_id'(foriegn-key) )
        db_user_reg=user_reg.objects.get(user_id=int(user_id))
        print(db_user_reg)

        # Re-assigning and saving data into specific user_reg table field (With the help of object(db_user_reg))
        db_user_reg.u_name=name
        db_user_reg.u_address=address
        db_user_reg.u_phone=phone
        db_user_reg.u_pincode=pincode
        db_user_reg.save()
        print('my effort worked')


        profile_authuser=User.objects.filter(username__contains=email)

        for y in profile_authuser:
            print(y.id,'try-1',type(y.id))
            
        return render(request,'userpanel/loggedhome/shoplistbody.html',{'sample':y}) 

    # return render(request,'userpanel/loggedhome/shoplistbody.html')


# Individual user data deletion purpose
def delete(request,value):
    # s=registration.objects.get(u_id=int(value))
    
    db_user_reg=user_reg.objects.get(user_id=int(value)) #deleteing user_reg table field
    print(db_user_reg)
    db_user_reg.delete()

    db_user=User.objects.get(id=int(value)) #deleteing User table field
    print(db_user)
    db_user.delete()

    return render(request,'userpanel/signup.html',{})


def logoutpage(request):
    shoplist=seller_reg.objects.all() # getting seller_reg table all data
    logout(request)
    return render(request,'userpanel/shoplistbody.html',{'shoplist':shoplist})

#////////////////// custom views - for a special purpose start ///////////////