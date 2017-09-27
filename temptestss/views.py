from django.shortcuts import render
from userss.models import UserProfile
# Create your views here.


def home(request):
    context = {}
    if str(request.user) != 'AnonymousUser':
        user = request.user
        user = UserProfile.objects.get(user=user)
        context = {'user': user}
    else:
        request.user = None
        context = {'user': request.user}

    return render(request, "home.html", context)
