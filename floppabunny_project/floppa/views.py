from django.shortcuts import render
from django.http import HttpResponse



#home page

def index(request):
    return HttpResponse("Home page loaded ok")



# about page branch

def about(request):
    return HttpResponse("About page loaded ok")

def commissions(request):
    return HttpResponse("Commissions page loaded ok")



# gallery branch
def gallery(request):
    return HttpResponse("Gallery page loaded ok")
    


# socials/contact branch

def more_floppa(request):
    return HttpResponse("Contact page loaded ok")
