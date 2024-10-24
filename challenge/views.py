from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for this month",
    "february": "Walk for at least 20 mintes every day",
    "march": None
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request , "challengeTest/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
    
def index(request): 
    months = list(monthly_challenges.keys())

    return render(request, "challengeTest/index.html", {
        "listofmonths": months
    })
    