from django.shortcuts import HttpResponseRedirect
from django.template.context_processors import csrf
from .models import Comment
from cardss.models import Cards
from userss.models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/users/login")
def write_comment(request, card_id):
    # import ipdb; ipdb.set_trace()
    context = {}

    if request.method == 'POST':
        card = Cards.objects.get(id=card_id)
        user = request.user
        user = UserProfile.objects.get(name=user)
        comment = request.POST.get('comm')

        new_comment = Comment(
            user=user,
            comment_on_card=card,
            comments=comment)
        new_comment.count += 1
        new_comment.save()
        context = {
            'comment': new_comment,
            "c_user": user
        }

    context.update(csrf(request))
    return HttpResponseRedirect("/cards/all/%s/" % card_id, context)
