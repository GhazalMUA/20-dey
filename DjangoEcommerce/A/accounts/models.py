from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email =models.EmailField(max_length=255, unique=True)
    phone_number =models.CharField(max_length=11 , unique=True)
    full_name= models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'       #fieldi ke mikhay user ro bahash etebar sanji bokoni , harchiziz inja gozashtim bayad tooye ghesmati ke tarifesh kardim unique esh true bashe
    
    REQUIRED_FIELDS = ['email' , 'full_name']           #fieldi ke mikhay  vaghti dari az dasture python manage.py createsuper user miani azat beporse

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,pbj=None):
        return True
    
    def has_module_perms(self, app_lable):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin