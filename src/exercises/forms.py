from django import forms


class QueryForm(forms.Form):
    CARDIO_CHOICE = "cardio"
    STRENGTHENING_CHOICE = "strengthening"
    BALANCED_CHOICE = "balanced"
    RATING_CHOICES = [
        (CARDIO_CHOICE, "Cardio"),
        (STRENGTHENING_CHOICE, "Strengthening"),
        (BALANCED_CHOICE, "Balanced"),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
