from django.db import models
import requests
# Create your models here.
from django.db import models
import datetime
from booking.models import UserCustomManager as UCM
# Create your models here.
from booking.models import Users
u = Users()
# import sqlite3 as sq
# con = sq.connect('db.sqlite3')
# cur = con.cursor()
# choices = (
#     ()
# )
class Feedback(models.Model):
    user= models.CharField(max_length=30)
    email = models.EmailField("email", max_length=54)
    feed = models.TextField("feedback",max_length=250)
    date = models.DateTimeField(default=datetime.datetime.now)
    stars = models.IntegerField("star",default=0)
    for_lawyer = models.CharField("for_lawyer",max_length=250,default=" ")  #ForeignKey(choices =choices ,u , on_delete)

    
    # objects = models.Manager()
    
    # REQUIRED_FIELDS = ['user','email','stars','for_lawyer']
    # x= Users.objects.total_rating_given.filter(name=for_lawyer)v
    # Users.objects.filter(name=for_lawyer).set_attrib(total_rating_given,)
    # lawyer1 = Users.objects.filter(is_lawyer=True and name = for_lawyer)
    # lawyer1.update(rating_stars ((Users.rating_stars*(Users.total_rating_given-1)+stars)/Users.total_rating_given))

    # .update(rating_stars=((Users.rating_stars*(Users.total_rating_given-1)+stars)/Users.total_rating_given))

    
