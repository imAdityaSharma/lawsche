from django.urls import re_path,include
from .views import *

urlpatterns = [
	re_path(r'^$',homepage,name='homepage'),
	re_path(r'^api/signup$',signup,name='signup'),
	re_path(r'^api/login$',userlogin,name='login'),
	re_path(r'^api/Damn-Developers$',developer,name='developer'),
	re_path(r'^api/dashboard1$',userdashboard,name='userdashboard'),
	re_path(r'^api/dashboard2$',lawyerdashboard,name='lawyerdashboard'),
	re_path(r'^api/acceptrequest/(?P<id>\d+)/$',acceptrequest,name='acceptrequest'),
	re_path(r'^api/denyrequest/(?P<id>\d+)/$',denyrequest,name='denyrequest'),
	re_path(r'^api/logout$',logout_view,name='logout'),
	re_path(r'^', include('chatty.urls'))


]