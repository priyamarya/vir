from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from .models import Cards
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from userss.models import UserProfile
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from commentss.models import Comment
from likess.models import CardLikes
from .forms import CardsForm

# Create your views here.


# @login_required(login_url="/users/login")
def all_cards(request):
    """This, function show all cards."""
    #import ipdb; ipdb.set_trace()

    context = {}
    
    cards = Cards.objects.all()

    paginator = Paginator(cards, 30)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        cards = paginator.page(page)
    except(EmptyPage, InvalidPage):
        cards = paginator.page(paginator.num_pages)
    context = {
        'cards': cards

    }
    context.update(csrf(request))

    return render(request, "allcards.html", context)



def view_card(request, card_id):
    """For displaying single card."""
    #import ipdb; ipdb.set_trace()

    context = {}
    if str(request.user) != "AnonymousUser":
        user = request.user
        user = UserProfile.objects.get(name=user)
    else:
        user = None
    card = Cards.objects.get(id=card_id)
    comment = card.name
    comment = Comment.objects.filter(comment_on_card=card)
    
    if (card.card_likes.filter(user=user).exists()):
        like_button = 'unlike'
    else:
        like_button = 'like'
    if card.v_type == "public":
        likers = []
        for item in CardLikes.objects.filter(like_on_card=card):
            likers.append(str(item.user))
        context = {
            'card': card,
            'like_button': like_button,
            'message': "public",
            "likers": likers,
            'comments': comment

        }
        context.update(csrf(request))
        return render(request, 'viewcard.html', context)
    else:
        if str(card.user) == str(request.user):
            context = {'message': "private", 'card': card}
            context.update(csrf(request))
            return render(request, 'viewcard.html', context)
        else:
            context = {'message': "Sorry. You are not authorised to see this card page."}
            context.update(csrf(request))
            return render(request, 'viewcard.html', context)


@login_required(login_url="/users/login/")
def new_card(request):
    #import ipdb; ipdb.set_trace()
    if request.method == "POST":

        context = {}
        
        form = CardsForm(request.POST, request.FILES or None)
        context = {
            "form": form,
            'message': "Please enter card information."

        }
        user = request.user
        user = UserProfile.objects.get(user=user)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            context = {
                'message': "Card is Saved",
                
            }
    else:
        
        context = {}
        # import ipdb; ipdb.set_trace()
        form = CardsForm()
        context = {
            "form": form,

            'message': "Please enter card information."

        }
        context.update(csrf(request))
        return render(request, "newcard.html", context)        

    context.update(csrf(request))
    return HttpResponseRedirect("/cards/all/")





def search(request):
   
    context = {}
    # import ipdb; ipdb.set_trace()

    if request.method == "POST":
        find = request.POST.get('find')
        cards = Cards.objects.filter(name__icontains=find)
        
        context = {
            'list': cards
        }
        context.update(csrf(request))

    return render(request, "show.html", context)


@login_required(login_url="/users/login/")
def edit_card(request,card_id):
    #import ipdb; ipdb.set_trace()
    instance=get_object_or_404(Cards,id=card_id)
    if Cards.objects.filter(id=card_id).exists():
        if request.method == "POST":
            context = {}
            instance=Cards.objects.get(id=card_id)
            form = CardsForm(request.POST or None, request.FILES, instance=instance)
            context = {
                "form": form,
                'message': "Please enter card information."

            }
            user = request.user
            user = UserProfile.objects.get(user=user)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                context = {
                    'message': "Card is Saved",
                    
                }
            else:
                context={
                    'message':"Please check the details entered by you."
                }
            context.update(csrf(request))
            return HttpResponseRedirect("/cards/all/%d/" %int(card_id))
        else:
            context = {}
            instance=Cards.objects.get(id=card_id)
            form = CardsForm(request.FILES,request.POST or None, instance=instance)
            context = {
                "form": form,
                'message': "Please enter card information."

            }
            user = request.user
            user = UserProfile.objects.get(user=user)
            context.update(csrf(request))
            return render(request,"editcard.html",context)
    else:
        context={'message': "no such blog available"}

    context.update(csrf(request))
    return render(request,"editcard.html",context)



