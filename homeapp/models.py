from django.db import models

# for importing auth_user table
from django.contrib.auth.models import User


# Create your models here.
class user_reg(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    u_id=models.AutoField(primary_key=True)
    u_name=models.CharField(max_length=200)
    u_address=models.CharField(max_length=200)
    u_phone=models.CharField(max_length=11)
    u_pincode=models.CharField(max_length=6)
    u_email=models.CharField(max_length=100,null=True,blank=True)

class seller_reg(models.Model):
    seller_id=models.ForeignKey(User,on_delete=models.CASCADE) #editted seller_id , auth_User table Foreign key fields, add imageFields(coverphoto,profilepic,idproof)
    s_id=models.AutoField(primary_key=True)
    s_fullname=models.CharField(max_length=200)
    s_shopname=models.CharField(max_length=200)
    s_address=models.CharField(max_length=200)
    s_location=models.CharField(max_length=200)
    s_coverphoto=models.ImageField(upload_to='coverphoto') #ImageField (Imp-1: Settings.py-(MEDIA_URL&MEDIA_ROOT))
    s_profilepic=models.ImageField(upload_to='profilepic') #ImageField (Imp-2: url.py-(import[settinsg&static],urlpatterns += static(settings.--------.MEDIA_ROOT) )
    
    # edited 2 field
    s_phone=models.CharField(max_length=10)
    s_aadhaar=models.CharField(max_length=15)

    s_idproof=models.ImageField(upload_to='idproof') #ImageField (Imp-3: submit_form(add enctype="multipart/form-data") in form)
    s_gstno=models.CharField(max_length=15)

    # edited 1 field
    s_pincode=models.CharField(max_length=6)

    s_state=models.CharField(max_length=100)
    s_district=models.CharField(max_length=100)
    s_taluk=models.CharField(max_length=100)
    s_email=models.CharField(max_length=100)

    sellerstate=models.CharField(max_length=30,null=True)# edited for approval(approval handling)

# class socialmedia_reg(models.Model):
#     sm_id=models.AutoField(primary_key=True)
#     sm_email=models.CharField(max_length=100)

# class debitcard(models.Model):
#     dc_id=models.AutoField(primary_kry=True)
#     dc_fullname=models.CharField(max_length=200)
#     dc_cardnumber=models.IntegerField(max_length=12)
#     dc_cvv=models.IntegerField(max_length=3)
#     dc_expirydate=models.IntegerField(max_length=4)

# class token(models.Model):
#     token_id=models.AutoField(primary_key=True)
#     # order_id=models.ForeignKey(order,on_delete=models.CASCADE)
#     # payment_id=models.ForeignKey(payment,on_delete=models.CASCADE)
#     token_no=models.IntegerField(max_length=3)
#     token_date=models.DateField(_(""), auto_now=False, auto_now_add=False)
    