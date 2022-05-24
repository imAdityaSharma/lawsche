from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.hashers import check_password,make_password 
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
# Create your models here.
class UserCustomManager(BaseUserManager):
	def create_user(self, name, email, is_lawyer=False, password=None):
		email = self.normalize_email(email)
		user = self.model(name=name,email=email,is_lawyer=is_lawyer)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,name, email, password,**extra_fields):	
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self.create_user(name,email,password)

		
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, is_lawyer, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#             is_lawyer=False,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, is_lawyer, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#             is_lawyer=True,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user



class Users(AbstractBaseUser):
	name = models.CharField(max_length=50,null=False, blank=False)
	email = models.EmailField(max_length=50,null=False,unique=True	)
	is_lawyer = models.BooleanField(default=False)
	startdate = models.DateField(null=True, blank=True)
	enddate = models.DateField(null=True, blank=True)
	# ratings for lawyer
	rating_stars = models.IntegerField(default=0)
	total_rating_given = models.IntegerField(default=0)
	# end here
	objects = UserCustomManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	#function to calculate avg rating of a lawyer
	# def set_attrib(self, attribute_string, value):
	# 	setattr(self,attribute_string,value)
	def rating_stars_for_lawyer(stars):
		rating_stars = int((stars+rating_stars)/total_rating_given)
		




	@classmethod
	def checkemail(cls,email):
		try:
			data = cls.objects.get(email=email)
		except:
			data = None
		return data

	@classmethod
	def check_user(cls,**kwargs):
		pw = kwargs.get('password')
		uid = kwargs.get('email')
		try:
			user = cls.objects.get(email=uid)
		except:
			return None
		if user.check_password(kwargs['password']):
			return user
		else:
			return None
		


	@classmethod
	def create_user(cls,data):
		return cls.objects.create_user(name=data['name'], email=data['email'], is_lawyer=data['is_lawyer'], password=data['password'])

	def __unicode__(self):
		return str(self.id)

class Bookingrequests(models.Model):
	description = models.TextField(max_length=100)
	from_userid = models.IntegerField(null=False, blank=False)
	from_email = models.EmailField(null=True)
	to_userid = models.IntegerField(null=False, blank=False)
	date = models.DateField(null=False, blank=False)
	accepted = models.BooleanField(default=False)
	denied = models.BooleanField(default=False)


	@classmethod
	def addrequest(cls,**kwargs):
		d = kwargs['data'].get('description',"None")
		f = kwargs['user']
		t = kwargs['data']['lawyer']
		date = kwargs['data']['date']
		e = kwargs['email']
		appointment = cls(description=d,from_userid=f,to_userid=t,date=date,from_email=e)
		appointment.save()
		# appointment.description = kwargs['data'].get('description',"None")
		# appointment.from_userid = kwargs['user']
		# appointment.to_userid = kwargs['data']['lawyer']
		# appointment.date = kwargs['data']['date']
		# appointment.save()
		# return appointment 


	def __unicode__(self):
		return str(self.id)