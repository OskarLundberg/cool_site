from django import forms
from django.core import validators


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave Empty",
                               validators=[validators.MaxLengthValidator(0, message="Should be left empty. "
                                                                                    "I suspect you might be a bot.")])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data["email"]
        verify_email = cleaned_data["verify_email"]

        if email != verify_email:
            raise forms.ValidationError("You need to enter the same email in both fields")





