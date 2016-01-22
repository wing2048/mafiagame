from django.shortcuts import render
from django.http import HttpResponse
from .models import Vote, VoteCount
from django.contrib.auth.models import User


def reset_vote_counts():
    VoteCount.objects.all().delete()
    for user in User.objects.all():
        if not user.is_superuser:
            VoteCount(user=user, votes=0).save()
    for vote in VoteCount.objects.all():
        vote.update_count()


# Create your views here.
def index(request):
    reset_vote_counts()
    votes = Vote.objects.order_by('time')
    votecounts = VoteCount.objects.order_by('votes')
    context = {
        'votes': votes,
        'votecounts': votecounts
    }
    return render(request, 'index.html', context=context)
