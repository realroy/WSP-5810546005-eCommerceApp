from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .form import contactForm


def contact(request):
    form = contactForm(request.POST or None)
    context = {'title': 'Contact', 'form': form }
    if form.is_valid():
        subject = 'Message from MYSITE.com'
        msg = '%s %s' %(form.cleaned_data['comment'], form.cleaned_data['name'])
        from_email = form.cleaned_data['email']
        to_email = [settings.EMAIL_HOST_USER]
        send_mail(subject, msg, from_email, to_email, fail_silently=False)
    return render(request, 'contact.html', context)
