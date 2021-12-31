"""groceryshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import admin_sellerapp.views

import homeapp.views

from django.conf.urls import url

from django.conf import settings # for image setting purpose
from django.conf.urls.static import static # for image setting purpose

urlpatterns = [
    path('admin/', admin.site.urls),
    # ////////////// admin_sellerapp path start //////////////////
        # {                    
    # *************** admin view path start ***************
    # admin dashboard
    path('admindashboard/',admin_sellerapp.views.admindashboard,name='admindashboard_url'),
    # add category
    path('addcategory/',admin_sellerapp.views.addcategory,name='addcategory_url'),
    # add notification
    path('addnotification/',admin_sellerapp.views.addnotification,name='addnotification_url'),
    # seller approval
    path('sellerapproval/',admin_sellerapp.views.sellerapproval,name='sellerapproval_url'),
    # seller approval view sub
    path('sellerapprovalview/',admin_sellerapp.views.sellerapprovalview,name='sellerapprovalview_url'),
    #view admin products
    path('adminproducts/',admin_sellerapp.views.adminproducts,name='adminproducts_url'),
    # view sellers_users
    path('sellers_users/',admin_sellerapp.views.sellers_users,name='sellers_users_url'),
    # view sales report
    path('salesreport/',admin_sellerapp.views.salesreport,name='salesreport_url'),
    # view transaction
    path('transaction/',admin_sellerapp.views.transaction,name='transaction_url'),
    # view transaction list sub
    path('transactionlist/',admin_sellerapp.views.transactionlist,name='transactionlist_url'),
    # contactus
    path('contactus/',admin_sellerapp.views.contactus,name='contactus_url'),
    # msgwindow contactus sub
    path('msgwindow/',admin_sellerapp.views.msgwindow,name='msgwindow_url'),
    # reports
    path('adminreports/',admin_sellerapp.views.adminreports,name='adminreports_url'),
    # add banner
    path('addbanner/',admin_sellerapp.views.addbanner,name='addbanner_url'),

    # //////////////// custom view paths start for (admin views side)//////////////////////
    url(r'^approval/(?P<value>\d+)/$',admin_sellerapp.views.approval_manager,name='approval_url'),
    # *************** admin view path end ***************

     # *************** seller view path start ***************
    #  seller dashboard
    path('sellerdashboard/',admin_sellerapp.views.sellerdashboard,name='sellerdashboard_url'),
    # sellerprofille
    path('sellerprofile/',admin_sellerapp.views.sellerprofile,name='sellerprofile_url'),
    # sellerprofille sub view
        #seller profile update
    path('sellerprofileupdate/',admin_sellerapp.views.sellerprofileupdate,name='sellerprofileupdate_url'),
    # sellerprofileupdate sub view
        # sellerpassword_view
    path('sellerpasswordview/<int:pk>',admin_sellerapp.views.sellerpassword_view,name='sellerpasswordview_url'),
    # sellerprofileupdate sub view
        # sellerpassword_reset
    path('sellerpasswordreset/',admin_sellerapp.views.sellerpassword_reset,name='sellerpasswordreset_url'),
    # sellerprofille sub view
        # sellerprofiledelete view
    path('sellerprofiledelete/<int:pk>',admin_sellerapp.views.sellerprofile_delete,name='sellerprofiledelete_url'),
    # add product
    path('addproduct/',admin_sellerapp.views.addproduct,name='addproduct_url'),
    # add offer
    path('addoffer/',admin_sellerapp.views.addoffer,name='addoffer_url'),
    # view orders
    path('orders/',admin_sellerapp.views.orders,name='orders_url'),
    # view order list sub
    path('orderslist/',admin_sellerapp.views.orderslist,name='orderslist_url'),
    # view customers
    path('customers/',admin_sellerapp.views.customers,name='customers_url'),
    # view payments
    path('payments/',admin_sellerapp.views.payments,name='payments_url'),
    # view products
    path('products/',admin_sellerapp.views.products,name='products_url'),
    
     # products view sub-
        # product_view
    url(r'^productview/(?P<value>\d+)/$',admin_sellerapp.views.product_view,name='productview_url'),

        # product_view sub view-1
    path('productupdate/',admin_sellerapp.views.product_update,name='productupdate_url'),

        # product_View sub view-2
    path('productdelete/<int:pk>',admin_sellerapp.views.product_delete,name='productdelete_url'),


    # view review
    path('reviews/',admin_sellerapp.views.reviews,name='reviews_url'),
    # view return
    path('returns/',admin_sellerapp.views.returns,name='returns_url'),
    # view notification
    path('notification/',admin_sellerapp.views.notification,name='notification_url'),
    # total sales
    path('totalsales/',admin_sellerapp.views.totalsales,name='totalsales_url'),
    # feedback_complaints
    path('feedback_complaints/',admin_sellerapp.views.feedback_complaints,name='feedback_complaints_url'),
    # reports
    path('sellerreports/',admin_sellerapp.views.sellerreports,name='sellerreports_url'),


    # *************** seller view path end ***************
        # }
    # ////////////// admin_sellerapp path end //////////////////







     # ////////////// homeapp path start //////////////////
    #  homepage
    path('homepage/',homeapp.views.homepage,name='homepage_url'),
    # homepage sub
        # Ajax loader for shoplistfilter view 
    path('shoplistfilter/',homeapp.views.shoplistfilter,name='shoplistfilter_url'),
        #  Ajax loader for productsfilter view 
    path('productsfilter/',homeapp.views.productsfilter,name='productsfilter_url'),
    # login
    path('login/',homeapp.views.loginpage,name='login_url'),
    # signup
    path('signup/',homeapp.views.userreg,name='signup_url'),
    # signupvendor
    path('signupvendor/',homeapp.views.sellerreg,name='signupvendor_url'),
    # shop products
    path('productlist/<int:pk>',homeapp.views.productlist,name='productlist_url'),
    # checkout
    path('checkoutpage/',homeapp.views.checkoutpage,name='checkoutpage_url'),
    # paymentpage
    path('paymentpage/',homeapp.views.paymentpage,name='paymentpage_url'),
    # COD
    path('cod/',homeapp.views.cod,name='cod_url'),
    # token page
    path('tokenpage/',homeapp.views.tokenpage,name='tokenpage_url'),
    # net banking
    path('netbanking/',homeapp.views.netbanking,name='netbanking_url'),
    # about
    path('aboutpage/',homeapp.views.aboutpage,name='aboutpage_url'),
    # contact
    path('contactuspage/',homeapp.views.contactuspage,name='contactuspage_url'),
    # ////////////// homeapp path end //////////////////


    # //////////////// custom view paths start for (homeapp view)//////////////////////
    # path('userregedit/',homeapp.views.userregedit,name='userregedit_url'),

    # for viewing user profile (read operation)
    url(r'^userregview/(?P<value>\d+)/$',homeapp.views.userregview,name='userregview_url'),
   
    # for updating user profile
    path('update/',homeapp.views.userregupdation,name='update_url'),
    
    #for deleting user profile
    url(r'^delete/(?P<value>\d+)/$',homeapp.views.delete,name='delete_url'),

    #for logout purpose
    path('logout/',homeapp.views.logoutpage,name='logout_url'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #(getting url address)Handling all mediafiles like(image,pdf,mp4,etc..)


# if settings.DEBUG: # for image setting purpose
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 