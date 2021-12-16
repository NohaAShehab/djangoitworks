from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
challenges = {
    "jan": "stop suger",
    "feb": "walk 30 min daily",
    "march": "sleep 10 hours daily"
}
mychallenges = {
    "jan": {"action": "stop suger", "img": "1.jpg", "desc": "stop"},
    "feb": {"action": "walk 30 min daily", "img": '2.jpg', "desc": "stop"},
    "march": {"action": "sleep 10 hours daily", "img": '3.jpg', "desc": "stop"},
    "april": {"action": "reduce social media", "img": '4.jpg', "desc": "stop"}
}


def getMonth(month):
    return challenges[month]


def monthchallengeNum(request, month):
    months = list(challenges.keys())
    try:
        ch = months[month - 1]
        # return HttpResponse(ch)
        # /challenges/jan
        url = reverse("monthchallenge", args=[ch])
        # return HttpResponseRedirect(f"/challenge/{ch}")
        return HttpResponseRedirect(url)
    except:
        return HttpResponseNotFound("not avaiable key")


def monthchallenge(request, month):
    try:
        ch = challenges[month]
        return HttpResponse(ch)
    except:
        return HttpResponseNotFound("not avaiable key")


def testurl(request, param):
    # return HttpResponse(param)
    return render(request, "challenges/testcss.html")


def extendbase(request):
    return render(request, "challenges/extendbase.html")


def index(request):
    # send data from views to the templates
    # send it in form of dictionary while rendering the page
    data = {"mydata": mychallenges}

    # for ch in challenges:
    #     print(ch, challenges[ch])

    return render(request, "challenges/listchallenges.html", context=data)


def challengedatails(request, challenge):
    # send parameters to the template
    # return HttpResponse(mychallenges[challenge])
    chdetails = mychallenges[challenge]
    return render(request, "challenges/challengedetails.html",
                  context={"challenge": chdetails, "month":challenge})

