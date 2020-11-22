from django import forms
from django.core.validators import MinValueValidator

from exercises.models import BodyRegion, Exercise


class QueryForm(forms.Form):
    CARDIO_CHOICE = "cardio"
    STRENGTHENING_CHOICE = "strengthening"
    BALANCED_CHOICE = "balanced"
    EVERYTHING_CHOICE = "everything"
    RATING_CHOICES = [
        (CARDIO_CHOICE, "Cardio"),
        (STRENGTHENING_CHOICE, "Strengthening"),
        (BALANCED_CHOICE, "Balanced"),
        (EVERYTHING_CHOICE, "Everything"),
    ]
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        initial=EVERYTHING_CHOICE,
        label="Catégorie",
    )
    body_regions = forms.ModelMultipleChoiceField(
        BodyRegion.objects.filter(
            id__in=Exercise.objects.values_list("body_regions", flat=True).distinct()
        ).order_by("name"),
        required=False,
        label="Région du corps",
    )
    number_of_exercises = forms.IntegerField(
        validators=[MinValueValidator(1)], initial=5, label="Nombre"
    )
