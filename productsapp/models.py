from django.db import models
# import registration.models

from admin_sellerapp.models import add_category
from homeapp.models import seller_reg

# import os

# Create your models here.

# def get_productimage_filepath(self,filename):
#     return 'Productimages/' + str(self.pk) +(filename)


class product(models.Model):
    pro_id=models.AutoField(primary_key=True)
    cat_id=models.ForeignKey(add_category,on_delete=models.CASCADE)
    seller_id=models.ForeignKey(seller_reg,on_delete=models.CASCADE)
    pro_category=models.CharField(max_length=100)
    pro_name=models.CharField(max_length=200)
    pro_details=models.CharField(max_length=200)
    pro_price=models.IntegerField(max_length=5)
    pro_rating=models.IntegerField(max_length=1,null=True,blank=True)
    pro_quantity=models.IntegerField(max_length=3)
    seller_email=models.CharField(max_length=100,null=True,blank=True)
    pro_image=models.ImageField(upload_to='Productimages')

# def upload_location(self,filename):
#     print("%s/%s"%(self.pk,filename))
#     return  "%s/%s" %(self.pk,filename)

# def upload_location(instance, filename):
#     #return "%s/%s.%s" %(instance.id, instance.id, extension)
#     if not instance.pk:
#         Model = instance.__class__
#         new_id=None
#         try:
#             new_id = Model.objects.order_by("id").last().id
#             if new_id:
#                 new_id += 1
#             else:
#                 pass
#         except:
#             new_id=1
#     else:
#         new_id = instance.pk
#     return "%s/%s/%s" %(Model.__name__, new_id, filename)



# def upload_directory_name(instance, filename):

#     user = getattr(instance, 'user', None)
#     if user:
#         name = f"{user.username}-{user.get_full_name().replace(' ', '-')}"
#     else:
#         name=str(instance)
#     model_name = instance._meta.verbose_name.replace(' ', '-')
#     return str(os.path.pathsep).join([model_name, name, filename])

# def directory_path(instance, filename):
#     return 'Productimages/instance_id_{0}/{1}'.format(instance.pk, filename)




# class offer(models.Model):
#     off_id=models.AutoField(primary_key=True)
#     product_id=models.ForeignKey(product,on_delete=models.CASCADE)
#     off_name=models.CharField(max_length=100)
#     off_amount=models.IntegerField(max_length=3)
#     # off_timeperiod=models.DurationField(_(""))
#     off_startdate=models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
#     off_enddate=models.DateTimeField(_(""), auto_now=False, auto_now_add=False)

# class cart(models.Model):
#     cart_id=models.AutoField(primary_key=True)
#     product_id=models.ForeignKey(product,on_delete=models.CASCADE)
#     quantity=models.IntegerField(max_length=3)
#     savelater=models.OneToOneField("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

# class order(models.Model):
#     order_id=models.AutoField(primary_key=True)
#     product_id=models.ForeignKey(product,on_delete=models.CASCADE)
#     offer_id=models.ForeignKey(offer,on_delete=models.CASCADE)
#     # user_id=models.ForeignKey(user_reg,on_delete=models.CASCADE)
#     order_date=models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
#     paymenttype=models.CharField(_(""), max_length=50)
#     pay_amount=models.IntegerField(_(""))
#     pay_status=models.CharField(_(""), max_length=50)

# class tracking(models.Model):
#     track_id=models.AutoField(primary_key=True)
#     product_id=models.ForeignKey(product,on_delete=models.CASCADE)
#     order_id=models.ForeignKey(order,on_delete=models.CASCADE)
#     shipping_info=models.CharField(max_length=100)
#     location=models.CharField(max_length=100)

# class payment(models.Model):
#     pay_id=models.AutoField(primary_key=True)
#     order_id=models.ForeignKey(order,on_delete=models.CASCADE)
#     payment_type=models.CharField(max_length=10)
#     transaction_id=models.IntegerField(max_length=100)
#     pay_amount=models.IntegerField(max_length=10)
#     pay_status=models.CharField(max_length=10)

# class review(models.Model):
#     review_id=models.AutoField(primary_key=True)
#     product_id=models.ForeignKey(product,on_delete=models.CASCADE)
#     # user_id=models.ForeignKey(user_reg,on_delete=models.CASCADE)
#     product_image=models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
#     message=models.CharField(max_length=100)
#     rating=models.IntegerField(max_length=1)

# class returns(models.Model):
#     return_id=models.AutoField(primary_key=True)
#     product_id=models.ForeignKey(product,on_delete=models.CASCADE)
#     order_id=models.ForeignKey(order,on_delete=models.CASCADE)
#     typeof_issue=models.CharField(max_length=50)

# class wishlist(models.Model):
#     wishlist_id=models.AutoField(primary_key=True)
#     product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    # user_id=models.ForeignKey(user_reg,on_delete=models.CASCADE)





    