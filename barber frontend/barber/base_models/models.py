from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class WebUser(AbstractUser):
    user_type = (
        ("User-customer", 1),
        ("Individual-barber", 2),
        ("Business-manger", 3),
    )

    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=500,null=True)
    password = models.CharField(max_length=500,null=True)
    user_type = models.IntegerField( choices=user_type,null=True)
    activate = models.CharField(max_length=500,null=True)
    designation = models.IntegerField(null=True)
    verification_code = models.IntegerField(null=True)
    created_time = models.DateTimeField(auto_now_add=True,auto_created=True)
    edited_time = models.DateTimeField(auto_created=False,auto_now=True)
       
    class Meta:
        db_table = 'web_user'

class WebUserDetails(models.Model):
    business_name = models.CharField(max_length=200,null=True)
    business_cell = models.CharField(max_length=200,null=True)
    business_address = models.CharField(max_length=200,null=True)
    business_website = models.CharField(max_length=200,null=True)
    postal_code = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    year_of_expereince = models.CharField(max_length=200,null=True)
    language = models.CharField(max_length=200,null=True)
    created_time = models.DateTimeField(auto_now_add=True,auto_created=True)
    edited_time = models.DateTimeField(auto_created=False,auto_now=True)
    web_user = models.ForeignKey(WebUser, related_name='web_user', on_delete=models.CASCADE, null=True)
    created_by= models.ForeignKey(WebUser, related_name="webuser_created_by", on_delete=models.SET_NULL, null=True)    
    updated_by= models.ForeignKey(WebUser, related_name="webuser_updated_by", on_delete=models.SET_NULL, null=True)    
    
    class Meta:
        db_table = 'web_user_detail'

class Designations(models.Model):
    designation_name = models.CharField(max_length=200,null=True)
    created_time = models.DateTimeField(auto_now_add=True,auto_created=True)
    edited_time = models.DateTimeField(auto_created=False,auto_now=True)
    created_by= models.ForeignKey(WebUser, related_name="designation_created_by", on_delete=models.SET_NULL, null=True)    
    updated_by= models.ForeignKey(WebUser, related_name="designation_updated_by", on_delete=models.SET_NULL, null=True)    

    class Meta:
        db_table = 'designation'           

class DesignationsCategory(models.Model):
    category_name = models.CharField(max_length=200,null=True)
    designation = models.ForeignKey(Designations, related_name='designation_set', on_delete=models.CASCADE, null=True)
    created_time = models.DateTimeField(auto_now_add=True,auto_created=True)
    edited_time = models.DateTimeField(auto_created=False,auto_now=True)
    created_by= models.ForeignKey(WebUser, related_name="designationcategory_created_by", on_delete=models.SET_NULL, null=True)    
    updated_by= models.ForeignKey(WebUser, related_name="designationcategory_updated_by", on_delete=models.SET_NULL, null=True)    

    class Meta:
        db_table = 'designation_category'       

class Services(models.Model):
    service_name = models.CharField(max_length=200,null=True)
    service_type = models.ForeignKey(DesignationsCategory, related_name='category_set', on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=200,null=True)
    time_duration = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    created_time = models.DateTimeField(auto_now_add=True,auto_created=True)
    edited_time = models.DateTimeField(auto_created=False,auto_now=True)
    created_by= models.ForeignKey(WebUser, related_name="service_created_by", on_delete=models.SET_NULL, null=True)    
    updated_by= models.ForeignKey(WebUser, related_name="service_updated_by", on_delete=models.SET_NULL, null=True)    

    class Meta:
        db_table = 'service'       



