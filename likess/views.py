from django.shortcuts import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from cardss.models import Cards
from userss.models import UserProfile
from .models import CardLikes

# Create your views here.


@login_required(login_url="/users/login")
def likes(request, card_id):
    # import ipdb; ipdb.set_trace()

    if request.method == "POST":

            card = Cards.objects.get(id=card_id)
            user = request.user
            user = UserProfile.objects.get(name=user)

            if card.card_likes.filter(user=user).exists():
                card.card_likes.get(user=user).delete()
                card.likes -= 1
                card.save()

                context = {
                    'success': True
                    # 'likes_by': liked_by
                }

            else:
                new_like = CardLikes(user=user, like_on_card=card)
                new_like.like += 1
                new_like.save()

                card.likes += 1
                card.save()

                context = {
                    'success': True
                }

    context.update(csrf(request))
    return HttpResponseRedirect("/cards/all/%s/" % card_id, context)
