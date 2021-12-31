from django.db import models

# for importing auth_user table
from django.contrib.auth.models import User
# Create your models here.

# //////////////// Admin model start /////////////////
# 1. addcategory
class add_category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=100)

# # 2.addnotification
# class addnotification(models.Model):
#     notif_id=models.AutoField(primary_key=True)
#     eventname=models.CharField(max_length=100)
#     eventimage=models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
#     startdate=models.DateField(_(""), auto_now=False, auto_now_add=False)
#     starttime=models.TimeField(_(""), auto_now=False, auto_now_add=False)
#     enddate=models.DateField(_(""), auto_now=False, auto_now_add=False)
#     endtime=models.TimeField(_(""), auto_now=False, auto_now_add=False)
#     message=models.CharField(max_length=200)

# # 3. approval
class approval(models.Model):
    approval_id=models.AutoField(primary_key=True)
    # seller_id=models.ForeignKey(seller_reg,on_delete=models.CASCADE)
    seller_id=models.ForeignKey(User,on_delete=models.CASCADE) # auth_User table Foreign key field
    sellerstate=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    # password=models.CharField(max_length=50)

# # 4. contactus
# class contactus(models.Model):
#     contact_id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=100)
#     email=models.EmailField(max_length=100)
#     message=models.CharField(max_length=100)

# # 5. msgtable
# class msgtable(models.Model):
#     msg_id=models.AutoField(primary_key=True)
#     # seller_id=models.ForeignKey(seller_reg,on_delete=models.CASCADE)
#     username=models.CharField(max_length=50)
#     commentmsg=models.CharField(max_length=100)

# # 6. addbanner
# class addbanner(models.Model):
#     banner_id=models.AutoField(primary_key=True)
#     eventname=models.CharField(max_length=50)
#     description=models.CharField(max_length=100)
#     bannerimage=models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

# # //////////////// Admin model end /////////////////


# # ///////////////// Seller model start //////////////

# # 1. feedback_complaints
# class feedback_complaints(models.Model):
#     fc_id=models.AutoField(primary_key=True)
#     issuetype=models.CharField(max_length=100)
#     message=models.CharField(max_length=100)

# ///////////////// Seller model start //////////////


