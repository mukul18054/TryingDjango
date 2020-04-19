from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home_view(request,*args,**kwargs):
	# return HttpResponse("this is home page")
	nums = {
	"name": "mukul",
	"mlist":['a','b',23]
	}
	return render(request, "home.html", nums)

def about_me_view(request,*args,**kwargs):
	# return HttpResponse("this is about me page")
	return render(request, "about_me.html", { 'name': "Mukul"})
