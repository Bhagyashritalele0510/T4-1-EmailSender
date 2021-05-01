from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def sendemail(request):
	if request.method =="POST":
		to=request.POST.get('toemail')
		subject=request.POST.get('subject')
		messege=request.POST.get('messege')
		#print(to,messege,subject)
		send_mail(
			#subject 
			subject,
			#msg
			messege,
			#fromemail
			settings.EMAIL_HOST_USER,
			#receivermail
			[to]
		)
		return render(
		request,
		'email.html',
		{

			'title' :'email sender'
		}
	    )

	else:
		return render(
		request,
		'email.html',
		{

			'title' :'email sender'
		}
	    )

	 