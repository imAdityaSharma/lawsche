from django.shortcuts import render
from .models import Feedback 
# from booking.models import Users
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.decorators import login_required
import datetime
# from .models import feedback

@login_required(login_url='login')
def feedback(request):
    print("Called")
    if request.method =="POST":
            
            email = request.POST.get('email')
            feed = request.POST.get('feedback')
            user = request.POST.get('user') 
            stars = request.POST.get('star')
            for_lawyer = request.POST.get('for_lawyer')
            # date = datetime.datetime.now()
            f = Feedback(email=email,feed=feed,user=user,stars=stars,for_lawyer=for_lawyer)
            f.save()
            print("Done")
            return HttpResponseRedirect('/')
    context={'context':'feedback',
        #      'lawyers' : Users.objects.all().filter(name=for_lawyer)
             }
    return render(request,'feedback.html',context=context)

def show_feedback(request):
    # x=Fb()
    print(Feedback.objects.all())
    context ={
        'feeds':Feedback.objects.all()
    }
    # def get_context_data(self,*args, **kwargs):
    #     context = super(Fb, self).get_context_data(*args,**kwargs)
    #     context['feeds'] = Fb.objects.all()
    #     return context
    return render(request, "feedback_review.html",context=context)
# from django.views.generic.base import TemplateView


# class show_feedback(TemplateView):
# 	template_name = 'feedback_review.html'
# 	def get_context_data(self,*args, **kwargs):
# 		context = super(show_feedback, self).get_context_data(*args,**kwargs)
# 		context['users'] = Fb.objects.all()
# 		return context
