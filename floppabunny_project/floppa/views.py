from django.shortcuts import render
from django.http import HttpResponse
from floppa.forms import UserForm, UserProfileForm


# register user
def register(request):
    registered = False # this is used to track if registration is successful - if it is this will become True

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True # here it is updated!

        else:
            print(user_form.errors, profile_form.errors)
        
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'floppa/register.html', context = {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered})

#home page

def index(request):
    context_dict = {'boldmessage': 'This also ran ok!'}
    return render(request, 'floppa/index.html', context=context_dict)



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
