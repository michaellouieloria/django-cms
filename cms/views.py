from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from cms.forms import ContactForm

def home(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about.html')

# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@simplesite.com'),
#                 ['administrator@simplesite.com'], #email address where message is sent.
#             )
#             return HttpResponseRedirect('/thanks/')
#     return render(request, 'contact.html',
#         {'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@simplesite.com'),
                ['administrator@simplesite.com'], #email address where message is sent.
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def thanks(request):
    return render_to_response('thanks.html')

def loggedin(request):
    return render_to_response('registration/loggedin.html',
                              {'username': request.user.username})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')

