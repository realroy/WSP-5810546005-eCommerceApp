from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def checkout(request):
    context = {'user': request.user}
    return render(request, 'checkout.html', context)