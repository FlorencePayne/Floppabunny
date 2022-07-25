from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from floppa.forms import UserForm, UserProfileForm


# user authentication branch
def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        # if statement to check if the sign up form is valid and to register the user
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'floppa/register.html', context = {'user_form': user_form,
                                                            'profile_form': profile_form,
                                                                'registered': registered})

    
def signin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('floppa:index'))
            else:
                return HttpResponse("Your Floppabunny account is disabled.")
        else:
            print(f"Incorrect login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'floppa/signin.html')


#can only logout if you're logged in
@login_required
def signout(request):
    logout(request)
    return redirect(reverse('floppa:index'))

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
