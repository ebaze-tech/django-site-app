from django.shortcuts import render, redirect
from .models import Meetup, Participant
from .forms import RegistrationForm
from django.http import Http404  # Import for handling exceptions
# from django.http import HttpResponse
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, "meetups/index.html", {
        'meetups': meetups
    })
print(index)

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
        #    user_email = registration_form.cleaned_data[ 'email']
        #    participant = Participant.objects.get_or_create(email=user_email)
            participant = registration_form.save()
            selected_meetup.participants.add(participant)
            return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
    except Exception as exc:
        # print(exc)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
print(meetup_details)

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
      'organizer_email': meetup.organizer_email
  })
print(confirm_registration)