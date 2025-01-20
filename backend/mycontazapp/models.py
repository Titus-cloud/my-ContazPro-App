from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# TODO: Creation of users and super users
class CustomUserManager(BaseUserManager):
  def creat_user(self,password = None, **extras):
    if not email:
      raise ValueError('Email must be set')
    email = self.normalize_email(email)
    user = self.model(email = email, **extras)
    user.set_password(password)
    user.save(using = self._db)
    return user


  def create_super_user(self,email, password=None, **extras):
    extras.setdefault('is_staff', True)
    extras.setdefault('is_superuser', True)
    if extras.get('is_staff') is not True:
      raise ValueError('Super user must have is_staff set to True')
    if extras.get('is_superuser') is not True:
      raise ValueError('Super user must have is_superuser set to True')

    return self.creat_user(email, password, **extras)

# Creating custom users
class CustomUser(AbstractBaseUser, PermissionsMixin):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_email_verified = models.BooleanField(default=False)
  objects = CustomUserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

  

#TODO: Function to take the picture and create a path for it
def contact_image(instance, filename):
  return 'contact/{filename}'.format(filename=filename)


class Category(models.Model):
  category_name = models.CharField(max_length=60)
  
  def __str__(self):
    return self.category_name

# Create your models here.
#FIXME: creating for users who are to be added their details
class Contact(models.Model):
  first_name = models.CharField(max_length=60)
  last_name = models.CharField(max_length=60)
  email = models.EmailField(unique=True, blank=True, null=True)
  phone_number = models.IntegerField(max_length=10, unique=True, blank=True, null=True)
  gender = models.CharField(blank=True, null=True)
  date_added = models.DateField(auto_now_add = True) #we will addd the exact time such that the user don't
  birthday = models.DateField(null=True, blank=True)
  address = models.TextField(null=True, blank=True)
  image = models.ImageField(upload_to=contact_image, default='contact/default.png')
  category = models.ManyToManyField(Category, null=True, blank=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"




