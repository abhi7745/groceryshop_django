from django.shortcuts import render, redirect

# importing admin_sellerapp all models
from admin_sellerapp.models import *

from homeapp.models import * #getting all homeapp models

from productsapp.models import * #getting all productsapp models


# sellerapp imports
import os # this method is for image updation(seller prodcut update)

from django.contrib import messages

from django.db.models import Q # this is for using mysql not equal to conditions

# importing password encryptor
from django.contrib.auth.hashers import make_password, check_password 

from homeapp.views import delete, logoutpage

# Create your views here.

# //////////////// admin view path start ////////////////
# admin dashboard
def admindashboard(request):
    return render(request,'adminpanel/dashboard.html',{})

# add category
def addcategory(request):
    if request.method=='POST':
        catname=request.POST.get('catname')
        
        print(catname)

        if(catname==''):
            print('no value')
            catdata=add_category.objects.all()
            return render(request,'adminpanel/addcategory.html',{'checker':'Invalid Info','catvalue':catdata})

        elif add_category.objects.filter(category_name__icontains=catname):
            print('Already Exist')
            catdata=add_category.objects.all()
            return render(request,'adminpanel/addcategory.html',{'checker':'Already Exist','catvalue':catdata})
        
        else:
            catobject=add_category()
            catobject.category_name=catname
            catobject.save()
            print('cat success')
            catdata=add_category.objects.all()
            return render(request,'adminpanel/addcategory.html',{'catvalue':catdata})
        

        # return render(request,'adminpanel/addcategory.html',{})

    catdata=add_category.objects.all()
    # for catvalue in catdata:
    #     print(catvalue.category_name)

    return render(request,'adminpanel/addcategory.html',{'catvalue':catdata})


#addnotification
def addnotification(request):
    if request.method=='POST':
        eventname=request.POST.get('eventname')
        eventimage=request.POST.get('eventimage')
        startdate=request.POST.get('startdate')
        starttime=request.POST.get('starttime')
        enddate=request.POST.get('enddate')
        endtime=request.POST.get('endtime')
        message=request.POST.get('message')

        print(eventname)
        print(eventimage)
        print(startdate)
        print(starttime)
        print(enddate)
        print(endtime)
        print(message)
    return render(request,'adminpanel/addnotification.html',{})

# seller approval
def sellerapproval(request):
    # approval_tbl=approval.objects.filter(sellerstate='Deactive')
    # for x in approval_tbl:
    #     # print(x.seller_id)
    #     seller_tbl=seller_reg.objects.filter(seller_id=x.seller_id)
        # for y in seller_tbl:
        #     print('id :',y.s_id)
        #     print('shopname :',y.s_shopname)
        #     print('fullname :',y.s_fullname)
        #     print('address :',y.s_address)
        #     print('gstno :',y.s_gstno)
        #     print('phone :',y.s_phone)

        #     print('--------------------')

    # deactive seller list filtering from seller_reg (purpose: for seller approval accepting section)
    seller_tbl=seller_reg.objects.filter(sellerstate='Deactive')

    # active user list filtering from seller_reg (purpose: for printing active seller)
    seller_active=seller_reg.objects.filter(sellerstate='active')
    # suspend user list filtering from seller_reg (purpose: for printing suspend seller)
    seller_sus=seller_reg.objects.filter(sellerstate='suspend')

    # common dictionary
    context={'seller_tbl':seller_tbl,'seller_active':seller_active,'seller_sus':seller_sus}


            # return render(request,'adminpanel/sellerapproval.html')
    
    return render(request,'adminpanel/sellerapproval.html',context)

# custom funtions for seller approval (seller approval handler)
def approval_manager(request,value):
    data=seller_reg.objects.get(s_id=int(value))
    print(data.s_shopname)
    print(data.s_fullname)

    data.sellerstate='active'
    data.save()
    print('new seller approved')

    # deactive seller list filtering from seller_reg (purpose: for seller approval accepting section)
    seller_tbl=seller_reg.objects.filter(sellerstate='Deactive')

    # active user list filtering from seller_reg (purpose: for printing active seller)
    seller_active=seller_reg.objects.filter(sellerstate='active')
    # suspend user list filtering from seller_reg (purpose: for printing suspend seller)
    seller_sus=seller_reg.objects.filter(sellerstate='suspend')

    # common dictionary
    context={'seller_tbl':seller_tbl,'seller_active':seller_active,'seller_sus':seller_sus}

    
    return render(request,'adminpanel/sellerapproval.html',context)

# seller approval view sub
def sellerapprovalview(request):
    return render(request,'adminpanel/sellerapprovalview.html',{})

# view admin products
def adminproducts(request):
    return render(request,'adminpanel/viewadminproducts.html',{})
# view seller_users
def sellers_users(request):
    return render(request,'adminpanel/viewsellers_users.html',{})
# view sales report
def salesreport(request):
    return render(request,'adminpanel/viewsalesreport.html',{})
# view transaction
def transaction(request):
    return render(request,'adminpanel/viewtransaction.html',{})
# view transaction list sub
def transactionlist(request):
    return render(request,'adminpanel/viewtransactionlist.html',{})
# contactus
def contactus(request):
    return render(request,'adminpanel/contactus.html',{})
# msgwindow contactus sub
def msgwindow(request):
    return render(request,'adminpanel/msgwindow.html',{})
# reports
def adminreports(request):
    return render(request,'adminpanel/reports.html',{})
# add banner
def addbanner(request):
    if request.method=='POST':
        eventname=request.POST.get('eventname')
        description=request.POST.get('description')
        bannerimage=request.POST.get('bannerimage')
        print(eventname)
        print(description)
        print(bannerimage)
    return render(request,'adminpanel/addbanner.html',{})

   
    
# //////////////// admin view path end ////////////////


# //////////////// seller view path start ////////////////
# dashboard
def sellerdashboard(request):
    sellerdata=seller_reg.objects.get(s_email=request.user)#identifying which user is this.(individual seller profile)
    print(sellerdata.s_id)
    # a=productslist.s_id

    sellerproduct=product.objects.filter(seller_id=sellerdata.s_id) # filter with seller id (productslist holds user data)
    pro_count=sellerproduct.count() # pro_count holds seller all product count number(only number value will return )
    # print(sellerproduct.count())
    return render(request,'sellerpanel/dashboard.html',{'pro_count':pro_count})

# sellerprofile
def sellerprofile(request):
    sellerdata=seller_reg.objects.get(s_email=request.user)#identifying which user is this.(individual seller profile)
    print(sellerdata.s_id,sellerdata.s_fullname)
    return render(request,'sellerpanel/sellerprofile.html',{'sellerdata':sellerdata})

# sellerprofile subview (updating seller_reg)
def sellerprofileupdate(request):
    if request.method=='POST':
        sid=request.POST.get('sellerid') # sellerid is for updating (filter purpose)
        sname=request.POST.get('fullname')
        shopname=request.POST.get('shopname')
        shopaddress=request.POST.get('shopaddress')
        shoplocation=request.POST.get('shoplocation')

        #imagefields
        #coverphoto=request.FILES['coverphoto']# ImageField or FileField - vannal must aayi request.FILES["name of input type="file"]
        #profilepicture=request.FILES['profilepicture'] # because request.FILES[""] -illotta files varunnatth.      
        #idproof=request.FILES['idproof']# don't use this method : idproof=request.POST.get('image') totally worng xxxxxxxxxxxxxxxxxx

        sphone=request.POST.get('sphone')
        aadhaar=request.POST.get('aadhaar')
        gst=request.POST.get('gst')
        spincode=request.POST.get('spincode')
        state=request.POST.get('state')
        district=request.POST.get('district')
        taluk=request.POST.get('taluk')
        semail=request.POST.get('semail')
        # spassword=request.POST.get('spassword')

        # abc=request.FILES.get('coverphoto')
        # print(abc)

        print(sid)
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

    # User table
    user_tbl=User.objects.get(username=request.user) # updating username from User table
    print(user_tbl.username,'login')

    if user_tbl.username != semail: # match condition for User table
        if semail.endswith('@gmail.com'):
            user_tbl.username = semail
            user_tbl.save()
            print('username match Saved')
        else:
            invalid_email='Invalid Email'
            sellerdata=seller_reg.objects.get(s_email=request.user)#identifying which user is this.(individual seller profile)
            print('invalid_email')    
            return render(request,'sellerpanel/sellerprofile.html',{'sellerdata':sellerdata,'invalid_email':invalid_email})
    
    # seller_reg table
    seller_update=seller_reg.objects.get(s_id=sid) # updating seller_reg all fields
    print(seller_update.s_fullname,'success')

    # All match if conditons for saving old seller_reg data to new.
    if seller_update.s_fullname != sname:   # fullname
        seller_update.s_fullname=sname
        print('fullname match Saved')

    if seller_update.s_shopname != shopname:    # shopname
        seller_update.s_shopname=shopname
        print('shopname match Saved')
    
    if seller_update.s_address != shopaddress:  # shopaddress
        seller_update.s_address=shopaddress
        print('shopaddress match Saved')

    if seller_update.s_location != shoplocation:    # shoplocation
        seller_update.s_location=shoplocation
        print('shoplocation match Saved')

    if seller_update.s_phone != sphone:    # sphone
        seller_update.s_phone=sphone
        print('sphone match Saved')    

    if seller_update.s_aadhaar != aadhaar:    # aadhaar
        seller_update.s_aadhaar=aadhaar
        print('aadhaar match Saved')    


    if seller_update.s_gstno != gst:    # gst
        seller_update.s_gstno=gst
        print('gst match Saved')  
          
    if seller_update.s_pincode != spincode:    # spincode
        seller_update.s_pincode=spincode
        print('spincode match Saved')   

    if seller_update.s_state != state:    # state
        seller_update.s_state=state
        print('state match Saved')    

    if seller_update.s_district != district:    # district
        seller_update.s_district=district
        print('district match Saved')  

    if seller_update.s_taluk != taluk:    # taluk
        seller_update.s_taluk=taluk
        print('taluk match Saved')  

    if seller_update.s_email != semail:    # semail
        seller_update.s_email=semail
        print('semail match Saved')    
    
    # Three image saving if conditions are here ( start ----------)
    if request.FILES.get('coverphoto') is not None: # coverphoto
        if len(request.FILES) != 0 :
                if len(seller_update.s_coverphoto) > 0: # it will check the old product image is not empty or not
                    os.remove(seller_update.s_coverphoto.path) # it will remove the old coverphoto image (imp:- import os)
                    # seller_update.s_coverphoto=request.FILES['coverphoto']# this will ditrectly save the image file from Form
                # seller_update.s_coverphoto=request.FILES.get('coverphoto')
                seller_update.s_coverphoto=request.FILES['coverphoto']
                print('coverphoto updated')

    if request.FILES.get('profilepicture') is not None: # profilepicture
        if len(request.FILES) != 0 :
                if len(seller_update.s_profilepic) > 0: # it will check the old product image is not empty or not
                    os.remove(seller_update.s_profilepic.path) # it will remove the old coverphoto image (imp:- import os)
                    # seller_update.s_coverphoto=request.FILES['coverphoto']# this will ditrectly save the image file from Form
                # seller_update.s_coverphoto=request.FILES.get('coverphoto')
                seller_update.s_profilepic=request.FILES['profilepicture']
                print('profilepicture updated')
    
    if request.FILES.get('idproof') is not None: # idproof
        if len(request.FILES) != 0 :
                if len(seller_update.s_idproof) > 0: # it will check the old product image is not empty or not
                    os.remove(seller_update.s_idproof.path) # it will remove the old coverphoto image (imp:- import os)
                    # seller_update.s_coverphoto=request.FILES['coverphoto']# this will ditrectly save the image file from Form
                # seller_update.s_coverphoto=request.FILES.get('coverphoto')
                seller_update.s_idproof=request.FILES['idproof']
                print('idproof updated')

    # Three image saving if conditions are here ( End ----------)
    
    seller_update.save()
    print('seller update')
    


    sellerdata=seller_reg.objects.get(s_email=semail)#identifying which user is this.(individual seller profile)
    print(sellerdata.s_id,sellerdata.s_fullname)    
    return render(request,'sellerpanel/sellerprofile.html',{'sellerdata':sellerdata})


# sellerprofileupdate subview (Resetting Password) in User table 
def sellerpassword_view(request,pk):
    print(pk)

    return render(request,'sellerpanel/resetform.html',{'pk':pk})

# sellerpassword_view sub View
def sellerpassword_reset(request):
    if request.method=='POST':
        sellerid=request.POST.get('sellerid') # id will filter correct user from User table
        psdnew=request.POST.get('psd_new')
        psdchecker=request.POST.get('psd_checker')
        print(psdnew)
        print(psdchecker)
        print(sellerid)

        if psdnew == '' and psdchecker == '':
            print('Please enter new password')
            return render(request,'sellerpanel/resetform.html',{'checker':'Please enter new password'})

        elif len(psdnew) < 4 and len(psdchecker) < 4:
            print('Please enter minimum 4 characters')
            return render(request,'sellerpanel/resetform.html',{'checker':'Please enter minimum 4 characters'})

        elif psdnew == psdchecker:
            seller_pass=User.objects.get(id=sellerid)
            print(seller_pass.id,'editing id')

            passEncrypted = make_password(psdnew)

            seller_pass.password=passEncrypted
            seller_pass.save()


            sellerdata=seller_reg.objects.get(s_email=seller_pass.username)#identifying which user is this.(individual seller profile)
            print(sellerdata.s_id,sellerdata.s_fullname)    
            print(request.user,'who is this')
            return render(request,'sellerpanel/sellerprofile.html',{'sellerdata':sellerdata,
            'passwordupdated':'Password Updated Successfully'})
        
        else:
            print('psd not matched')
            return render(request,'sellerpanel/resetform.html',{'checker':'password not matched'})

    return render(request,'sellerpanel/resetform.html',{})

# sellerprofile subview (Deleting seller_reg table, User table, Product table, etc coming soon...)
def sellerprofile_delete(request,pk):
    print(pk,'pk id')

    # seller_reg delete (Start)#####################################################
    db_seller_reg=seller_reg.objects.get(seller_id_id=pk)
    print(db_seller_reg.s_email)

    # Deleting seller_reg all images (Start)------------- uncomment soon......
    # coverphoto delete(path and db side)
    # if len(request.FILES) == 0 :
    #     if len(db_seller_reg.s_coverphoto) > 0: # it will check the old product image is not empty or not
    #         # os.remove(db_seller_reg.s_coverphoto.path) # it will remove the old coverphoto image (imp:- import os)      
    #         # db_seller_reg.s_coverphoto.delete()
    #         print('coverphoto deleted')
    
    # # profilepic delete(path and db side)
    # if len(request.FILES) == 0 :
    #     if len(db_seller_reg.s_profilepic) > 0: # it will check the old product image is not empty or not
    #         # os.remove(db_seller_reg.s_profilepic.path) # it will remove the old coverphoto image (imp:- import os)
    #         # db_seller_reg.s_profilepic.delete()
    #         print('profilepicture deleted')

    # # idproof delete(path and db side)
    # if len(request.FILES) == 0 :
    #     if len(db_seller_reg.s_idproof) > 0: # it will check the old product image is not empty or not
    #         # os.remove(db_seller_reg.s_idproof.path) # it will remove the old coverphoto image (imp:- import os)
    #         # db_seller_reg.s_idproof.delete()
    #         print('idproof deleted')
    # Deleting seller_reg all images (End)-------------

    # product delete (Start)----------------------------
    db_seller_products=product.objects.filter(seller_email=db_seller_reg.s_email)

    if product.objects.filter(seller_email=db_seller_reg.s_email).exists():
        for x in db_seller_products:
            print(x.pro_name,'Products')

            # deleting product images(path and db side )
            if len(request.FILES) == 0 : # this line will check there is a file data is empty(imagefileld) ie; Equal to Zero Case
                if len(x.pro_image) > 0: # it will check the old product image is not empty or not
                    os.remove(x.pro_image.path) # delete old image from media folder (path: Prod )
                # x.pro_image.delete()
                print('image path Deleted')


            x.delete() #deleteting all seller product from database (product tbl) 
            print('product tbl row deleted success')
    else:
        print('No product found in database')
    # product delete (End)----------------------------

    # db_seller_reg.delete() uncomment soon......
    print('seller data deleted from seller_reg table')
    # seller_reg delete (End)#####################################################

    # User delete (Start)#####################################################
    db_user_table=User.objects.get(id=pk)
    print(db_user_table.id,'user id')
    # db_user_table.delete()   uncomment soon......
    print('User table seller data deleted')
    # User delete (End)#####################################################


    return redirect(logoutpage)

    
# add product
def addproduct(request):
    # calling admincatergory model
    admincategory=add_category.objects.all() # calling all add_category table value for choosing category in --
                                             #  seller product add form

    if request.method=='POST':
        category=request.POST.get('category')
        productname=request.POST.get('productname')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')

        # imageField
        productimage=request.FILES['productimage']

        discription=request.POST.get('discription')
        print(category)
        print(productname)
        print(price)
        print(quantity)
        print(productimage)
        print(discription)

        # geting category table from model
        cat_object=add_category.objects.get(category_name=category)
        print(cat_object)
        # geting seller_reg table from models
        seller_object=seller_reg.objects.get(s_email=request.user)
        print(seller_object.s_email)

        # Creating product table object
        product_object=product()

        product_object.cat_id=cat_object # cat_object holds add_category table object (eg: vegitable-id = 1 )
        product_object.seller_id=seller_object # seller_object holds seller_reg table object (eg: seller-id  = 2 )

        product_object.pro_category=category
        product_object.pro_name=productname
        product_object.pro_details=discription
        product_object.pro_price=price
        product_object.pro_rating='1'
        product_object.pro_quantity=quantity
        product_object.pro_image=productimage
        product_object.seller_email=seller_object.s_email
        product_object.save()
        
        messages.success(request, "Your product added successfully!")
        
        # return render(request,'sellerpanel/viewproducts.html',{})


    return render(request,'sellerpanel/addproduct.html',{'admincategory':admincategory})
# add offer
def addoffer(request):
    if request.method=='POST':
        productname=request.POST.get('productname')
        offername=request.POST.get('offername')
        offeramount=request.POST.get('offeramount')
        startdate=request.POST.get('startdate')
        starttime=request.POST.get('starttime')
        enddate=request.POST.get('enddate')
        endtime=request.POST.get('endtime')
        print(productname)
        print(offername)
        print(offeramount)
        print(startdate)
        print(starttime)
        print(enddate)
        print(endtime)
    return render(request,'sellerpanel/addoffer.html',{})
# view order
def orders(request):
    return render(request,'sellerpanel/vieworder.html',{})
# viewv order list sub
def orderslist(request):
    return render(request,'sellerpanel/vieworderlist.html',{})
# view customers
def customers(request):
    return render(request,'sellerpanel/viewcustomers.html',{})
# view payments
def payments(request):
    return render(request,'sellerpanel/viewpayments.html',{})

# view products
def products(request):
    # productslist=product.objects.all()
    sellerdata=seller_reg.objects.get(s_email=request.user)#identifying which user is this.(individual seller profile)
    print(sellerdata.s_id)
    # a=productslist.s_id

    sellerproduct=product.objects.filter(seller_id=sellerdata.s_id) # filter with seller id (productslist holds user data)
    pro_count=sellerproduct.count() # pro_count holds seller all product count number(only number value will return )
    # print(sellerproduct.count())

    admincategory=add_category.objects.all() # calling all add_category table value for choosing category in --
    print(admincategory,'hai')                                    #  seller product filter form

    # special filtering form area (filter purpose only)
    if request.method=='POST':
        form_cat=request.POST.get('form_category')
        print(form_cat,'option Value from Form')

        if form_cat == None :
            # cat_productsall=product.objects.all()
            print('Null value')
            return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':sellerproduct,'pro_count':pro_count,
            'all_count':pro_count,'admincategory':admincategory})

        elif form_cat== 'All':
            # cat_productsall=product.objects.all()
            print('all cat')
            return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':sellerproduct,'pro_count':pro_count,
            'all_count':pro_count,'admincategory':admincategory})
        else:
            cat_products=product.objects.filter(pro_category=form_cat)
            for x in cat_products:
                print(x.pro_name,'else cat')
            return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':cat_products,'cat_count':cat_products.count(),
            'pro_count':pro_count,'admincategory':admincategory})

    

    return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':sellerproduct,'pro_count':pro_count,
    'all_count':pro_count,'admincategory':admincategory})

# sub view of products function_view (above view)
def product_view(request,value):
    # print(value)

    productdetails=product.objects.filter(pro_id=int(value)) # identifying which product is this using value from url 
    # print(productdetails)                                     # value holds seller_id
    for x in productdetails:
        print(x.pro_name,'product area')
    
    catdata=add_category.objects.filter(~Q(category_name=x.pro_category)) # passing categories to product view form where not equal to method
    # for y in catdata:
    #     print(y.category_name)
    # catdata=add_category.objects.raw("select * from admin_sellerapp_add_category where not category_name='x.pro_category' ") # passing all categories to product view form

    return render(request,'sellerpanel/product_view.html',{'x':x,'catdata':catdata})

# sub view of product_view function_view (above view)
def product_update(request):

    # Update area start---------
    sellerdata=seller_reg.objects.get(s_email=request.user)#identifying which user is this.(individual seller profile)
    # print(sellerdata.s_id)
    # a=productslist.s_id

    sellerproduct=product.objects.filter(seller_id=sellerdata.s_id) # filter with user id (sellerdata holds user data)
    pro_count=sellerproduct.count() # pro_count holds seller all product count number(only number value will return )
    # print(sellerproduct,'aaaaaaa')


    if request.method=='POST':
        product_id=request.POST.get('product_id') # id is getting from product update form

        category=request.POST.get('category')          #updating
        productname=request.POST.get('productname')    #updating
        price=request.POST.get('price')                #updating
        quantity=request.POST.get('quantity')          #updating
        discription=request.POST.get('discription')    #updating

        # imageField
        # productimage=request.FILES.['productimage'] Wrong way---I use it in the special if case for Re-saving image
        # productimage=request.FILES.get('productimage')    #updating     


        print(product_id)
        # print(category)
        # print(productname)
        # print(price)
        # print(quantity)
        # print(productimage)
        # print(discription)

        # case 1 use in normal way
        pro_update=product.objects.get(pro_id=int(product_id))
        print(pro_update,'success')

        if len(request.FILES) != 0: # this line will check there is a file data from form(imagefileld) ie; Not None Case
            if len(pro_update.pro_image) > 0: # it will check the old product image is not empty or not
                os.remove(pro_update.pro_image.path) # it will remove the old product image (imp:- import os)
            pro_update.pro_image=request.FILES['productimage'] # this will ditrectly save the image file from Form
            print('new image')

        pro_update.pro_category=category    
        pro_update.pro_name=productname
        pro_update.pro_details=discription
        pro_update.pro_price=price
        pro_update.pro_quantity=quantity
        pro_update.save()   
        print('product updated')        

        
        # case 2- use a url value for checking which product is this. Eg: path('productupdate/<str:pk>',...)
        # the pk varialble holds the specific product_id. that will helps to check which product is this.
        # imp note:- pass action="{% url 'productupdate_url' x.pro_id %}" in product_view.html form.
        # pro_update=product.objects.get(pro_id=pk)
        # print(pro_update,'success')

        # if len(request.FILES) != 0: # this line will check there is a file data from form(imagefileld)  
        #     if len(pro_update.pro_image) > 0:
        #         os.remove(pro_update.pro_image.path)
        #     # pro_update.pro_image=productimage
        #     pro_update.pro_image=request.FILES['productimage']
        #     print('new image')

        # pro_update.pro_category=category    
        # pro_update.pro_name=productname
        # pro_update.pro_details=discription
        # pro_update.pro_price=price
        # pro_update.pro_quantity=quantity
        # pro_update.save()
        # print('product updated')

        # update area end---------

    admincategory=add_category.objects.all() # calling all add_category table value for choosing category in --
    print(admincategory,'hai')                                    #  seller product filter form

    # special filtering form area (filter purpose only)
    if request.method=='POST':
        form_cat=request.POST.get('form_category')
        print(form_cat,'NOT POST')
        if form_cat== 'All':
            # cat_productsall=product.objects.all()
            print('all cat')
            return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':sellerproduct,'pro_count':pro_count,
            'all_count':pro_count,'admincategory':admincategory})
        else:
            cat_products=product.objects.filter(pro_category=form_cat)
            for x in cat_products:
                print(x.pro_name,'else cat')
                return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':cat_products,'cat_count':cat_products.count(),
                'pro_count':pro_count,'admincategory':admincategory})

    print('HERE')
    return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':sellerproduct,'pro_count':pro_count,
    'admincategory':admincategory,'all_count':pro_count})

# sub view of product_view function_view (above view)
def product_delete(request,pk):

    # delete area start---------
    sellerdata=seller_reg.objects.get(s_email=request.user)#identifying which user is this.(individual seller profile)
    # print(sellerdata.s_id)
    # a=productslist.s_id

    sellerproduct=product.objects.filter(seller_id=sellerdata.s_id) # filter with user id (sellerdata holds user data)
    # print(sellerproduct,'aaaaaaa')


    pro_delete=product.objects.get(pro_id=int(pk))
    if len(request.FILES) == 0: # this line will check there is a file data is empty(imagefileld) ie; Equal to Zero Case
        if len(pro_delete.pro_image) > 0: # it will check the old product image is not empty or not
            os.remove(pro_delete.pro_image.path) # delete old image from media folder (path: Prod )
        pro_delete.delete()
        print('product Deleted')
    # delete area end---------

    pro_count=sellerproduct.count() # pro_count holds seller all product count number(only number value will return )

    admincategory=add_category.objects.all() # calling all add_category table value for choosing category in --
    print(admincategory,'hai')                                    #  seller product filter form

    # special filtering form area (filter purpose only)
    if request.method=='POST':
        form_cat=request.POST.get('form_category')
        print(form_cat,'NOT POST')
        if form_cat== 'All':
            # cat_productsall=product.objects.all()
            print('all cat')
            return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':sellerproduct,'pro_count':pro_count,
            'all_count':pro_count,'admincategory':admincategory})
        else:
            cat_products=product.objects.filter(pro_category=form_cat)
            for x in cat_products:
                print(x.pro_name,'else cat')
                return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':cat_products,'cat_count':cat_products.count(),
                'pro_count':pro_count,'admincategory':admincategory})

    # Main Render
    return render(request,'sellerpanel/viewproducts.html',{'sellerproduct':sellerproduct,'pro_count':pro_count,
    'admincategory':admincategory,'all_count':pro_count})

# view review
def reviews(request):
    return render(request,'sellerpanel/viewreview.html',{})
# view return
def returns(request):
    return render(request,'sellerpanel/viewreturn.html',{})
# view notification
def notification(request):
    return render(request,'sellerpanel/viewnotification.html',{})
# total sales
def totalsales(request):
    return render(request,'sellerpanel/totalsales.html',{})
# feedback_complaints
def feedback_complaints(request):
    if request.method=='POST':
        myoption=request.POST.get('myoption')
        message=request.POST.get('message')
        print(myoption)
        print(message)
    return render(request,'sellerpanel/feedback_complaints.html',{})
# reports
def sellerreports(request):
    return render(request,'sellerpanel/reports.html',{})


# //////////////// seller view path end ////////////////


