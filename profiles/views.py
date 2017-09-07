from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)
