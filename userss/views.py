from django.shortcuts import render_to_response, HttpResponseRedirect, render, get_object_or_404
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.context_processors import csrf
from .models import UserProfile, UserProfileInfo
from .forms import UserProfileInfoForm

# Create your views here.


def register(request):
    context = {}
    #import ipdb; ipdb.set_trace()

    if request.method == 'POST':
        try:
            name = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if password2 == password1:
                user = User.objects.create_user(
                    username=name,
                    password=password1,
                    email=email)
                user_info = UserProfile(user=user, name=name, email=email)
                user_info.save()
                

                context = {'success': True, 'message': 'Your User Profile Created.'}
                context.update(csrf(request))
                return render_to_response("registration_done.html", context)
        except:
            context = {'success': False, 'message': "user Profile can't be saved. please SignUp again"}
            context.update(csrf(request))
            return render_to_response("registration_done.html", context)
    context.update(csrf(request))
    return render_to_response('register.html', context)


def login(request):
    context = {}
    # import ipdb; ipdb.set_trace()
    if request.method == "GET":
        if request.user.is_authenticated():
            context['user'] = request.user.username
            context.update(csrf(request))
            return render_to_response("login.html", context)
        else:
            context.update(csrf(request))
            return render_to_response("login.html", context)

    elif request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=name, password=password)
        if request.user.is_authenticated():
            context = {"status": "One user already logged in"}
            context['user'] = request.user.username
            context.update(csrf(request))
            return render_to_response("login.html", context)
        else:
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    context = {"status": "login successfull"}
                    context['user'] = request.user.username
                    context.update(csrf(request))
                    return HttpResponseRedirect('/cards/all/')
                else:
                    context = {"status": 'account de-activated'}
                    context.update(csrf(request))
                    return render_to_response("login.html", context)
            else:
                context = {"status": "invalid login details"}
                context.update(csrf(request))
                return render_to_response("login.html", context)
    else:

        context.update(csrf(request))
        return render_to_response("login.html", context)


@login_required(login_url='/users/login/')
def logout(request):
    # import ipdb; ipdb.set_trace()
    """Logout method for LoggedIn Users."""
    if request.user.is_authenticated():
        auth.logout(request)
        context = {}
        context['status'] = 'Logout sucessfull'
        context.update(csrf(request))
        return login(request)
    else:
        pass


def home(request):
    context = {}

    return render(request, "about.html", context)


def about(request):
    context = {}

    return render(request, "about.html", context)


def contact(request):
    context = {}

    return render(request, "contact.html", context)

@login_required(login_url='/users/login/')
def user_details_entry1(request):
    #import ipdb; ipdb.set_trace()
    title = "Please fill this form so that everybody can know about you."
    if request.method=="POST":
        form = UserProfileInfoForm(request.POST, request.FILES or None)
        context = {
            'title': title,
            'form': form
        }
        user = request.user
        user = UserProfile.objects.get(user=user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userlink = user
            instance.save()
            context = {
                'title': "thank you"
            }
        context.update(csrf(request))
        return HttpResponseRedirect("/users/user/%s"%str(request.user))
    else:
        form = UserProfileInfoForm(request.POST, request.FILES or None)
        context = {
            'title': title,
            'form': form
        }
    context.update(csrf(request))
    return render(request, 'userdetailsentry.html', context)

@login_required(login_url='/users/login/')
def user_details_entry(request):
    #import ipdb; ipdb.set_trace()
    
    context = {}
    if request.method == "POST":
        try:
            full_name = request.POST.get("full_name")
            pic = request.FILES.get("pic")
            sex = request.POST.get("sex")
            user = request.user
            user = UserProfile.objects.get(user=user)

            
            user = UserProfileInfo(
                userlink=user,
                full_name=full_name,
                gender=sex,
                profile_pic=pic)
            user.save()
            context = {
                "status": True, 'message': "Profile Saved."
            }
            context.update(csrf(request))
            return render_to_response("userdetailsentry.html", context)
        except:
            context = {
                "status": False, 'message': "Profile Not Saved."
            }
            context.update(csrf(request))
            return render_to_response("userdetailsentry.html", context)
    else:        
        user = request.user
        user = UserProfile.objects.get(user=user)
        if UserProfileInfo.objects.filter(userlink=user).exists():
            user = UserProfileInfo.objects.get(userlink=user)
            
            context={
                'user':user,
               
            }
            context.update(csrf(request))
            return render(request,"details.html", context)
        else:
            context={
            "title":"please fill the form below"
            }
            context.update(csrf(request))
            return render_to_response("userdetailsentry.html", context)
    context = {'message': "not saved"}
    context.update(csrf(request))
    return render_to_response("userdetailsentry.html", context)


@login_required(login_url='/users/login/')
def user(request, username):
    #import ipdb; ipdb.set_trace()

    context = {}
    user = username
    user = UserProfile.objects.get(name=user)
    if UserProfileInfo.objects.filter(userlink=user).exists():
        user = UserProfileInfo.objects.get(userlink=user)
        context = {
            'user': user,

        }
    else:
        title = "we dont know anything about you. please fill the details form"
        context = {'title': title}
    context.update(csrf(request))
    return render(request, "user.html", context)





@login_required(login_url='users/login/')
def profile_edit(request,username):
   # import ipdb; ipdb.set_trace()
    title = "Edit Our Profile Here"

    instance=get_object_or_404(User,username=username)
    instance = UserProfile.objects.get(user=instance)
    if UserProfileInfo.objects.filter(userlink=instance).exists():
        instance = UserProfileInfo.objects.get(userlink=instance)
        if request.method =="GET":
            form = UserProfileInfoForm(request.POST or None,request.FILES,instance=instance)
            context = {
                "title": title,
                "form": form,
                "instance":instance,
            }
            context.update(csrf(request))
            return render(request, "userdetailsentry.html",context)    
        else:

            user = request.user
            user = UserProfile.objects.get(user=user)
            form = UserProfileInfoForm(request.POST,request.FILES or None, instance=instance)
            if form.is_valid():
                instance = form.save(commit=False)
                
                instance.save()

            #print request.POST.get('full_name')
            #print request.POST.get('sex')
            context = {
                "instance":instance,
                "title": "thanks for telling us more about you.",
            }
            context.update(csrf(request))
            return HttpResponseRedirect("/users/user/%s/"%username)
    else:
        if request.method =="GET":
            form = UserProfileInfoForm(request.POST or None)
            context = {
                "title": title,
                "form": form,
                "instance":instance,
            }   
        else:
            user = request.user
            user = UsersProfile.objects.get(user=user)
            form = UserProfieInfoForm(request.POST,request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.userlink=user
                instance.save()

            #print request.POST.get('full_name')
            #print request.POST.get('sex')
            context = {
                "instance":instance,
                "title": "thanks for telling us more about you.",
            }

                
    context.update(csrf(request))
    return render(request, "user.html",context)

