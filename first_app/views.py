from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	my_dict = {'insert_me':'This text is from templates/first_app/index.html'}
	# return HttpResponse("Wannacum!!")
	return render(request,'first_app/index.html',context=my_dict)

def noPattern(request):
	return HttpResponse("This is triggered when no pattern is there for the first_app!")