from django.views import generic
from django.views.generic.edit import FormMixin

from exercises.forms import QueryForm
from exercises.models import Exercise


class RandomExercisesView(generic.ListView, FormMixin):
    model = Exercise
    context_object_name = "exercises"
    form_class = QueryForm

    def get_queryset(self):
        form = self.get_form()
        base_queryset = self.get_base_queryset(form)
        return base_queryset.order_by("?")[:5]

    def get_base_queryset(self, form):
        if not form.is_valid():
            return Exercise.objects.all()
        data = form.cleaned_data
        rating = data.get("rating")
        if rating == QueryForm.BALANCED_CHOICE:
            return Exercise.objects.get_balanced()
        elif rating == QueryForm.CARDIO_CHOICE:
            return Exercise.objects.get_mostly_cardio()
        elif rating == QueryForm.STRENGTHENING_CHOICE:
            return Exercise.objects.get_mostly_strengthening()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        get = self.request.GET
        if get:
            kwargs.update({"data": get})
        return kwargs
