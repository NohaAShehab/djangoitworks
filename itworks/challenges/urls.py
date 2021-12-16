from django.urls import path
from challenges.views import monthchallenge,monthchallengeNum,\
    testurl, index, challengedatails, extendbase


urlpatterns = [
    path("extendbase", extendbase, name="extendbase"),
    path("index", index, name="challengesindex"),
    path("index/<challenge>", challengedatails, name="challengedetails"),
    path("<int:month>", monthchallengeNum, name="monthchallengeNum"),
    path("<str:month>", monthchallenge, name="monthchallenge"),
    # validate url
    path("param/<int:param>", testurl),

]
