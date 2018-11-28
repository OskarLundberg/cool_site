from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.contrib import messages          #  Probably wont use this

from . import forms


def homepage(request):
    return render(request, "home.html")


def suggestion_view(request):
    form = forms.SuggestionForm()
    if request.method == "POST":
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            print("Badonkers")
            send_mail(
                'Suggestion from {}.'.format(form.cleaned_data["name"]),
                form.cleaned_data["suggestion"],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['MicrowavedHotDog@egg.com'],
            )
            return HttpResponseRedirect(reverse("suggest"))
    return render(request, "suggestion_form.html", {"form": form})
