from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, AccessRecord, Topic

# Create your views here.

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records':webpages_list}
	# my_dict = {'insert_me':'This text is from templates/first_app/index.html'}
	# return HttpResponse("Wannacum!!")
	return render(request,'first_app/index.html',context=date_dict)

def noPattern(request):
	return HttpResponse("This is triggered when no pattern is there for the first_app!")