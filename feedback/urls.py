from django.urls import path,include
from . import views
from django.http import HttpResponseRedirect

urlpatterns = [
	path('feedback',views.feedback,name="feedback"),
	path('feedbkndreview', views.show_feedback,name="feedbackANDreview"),
]