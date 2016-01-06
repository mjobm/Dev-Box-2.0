from django.db import models
class DevBoxUser(models.Model):
    user_name = models.CharField(max_length=50,blank=True)
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email_address = models.EmailField(max_length=50,blank=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class DevBoxCreatedAt(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True
