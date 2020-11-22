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
        if not form.is_valid():
            print(form.errors)
            for field in form:
                print(field.name, field.errors)
            return Exercise.objects.order_by("?")[:5]

        base_queryset = self.get_base_queryset(form)
        filters = {}
        body_regions = form.cleaned_data.get("body_regions")
        if body_regions:
            filters.update({"body_regions__in": body_regions})
        number_of_exercises = form.cleaned_data.get("number_of_exercises")
        return base_queryset.filter(**filters).order_by("?")[:number_of_exercises]

    def get_base_queryset(self, valid_form):
        data = valid_form.cleaned_data
        rating = data.get("rating")
        if rating == QueryForm.BALANCED_CHOICE:
            return Exercise.objects.get_balanced()
        elif rating == QueryForm.CARDIO_CHOICE:
            return Exercise.objects.get_mostly_cardio()
        elif rating == QueryForm.STRENGTHENING_CHOICE:
            return Exercise.objects.get_mostly_strengthening()
        else:
            return Exercise.objects.all()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        get = self.request.GET
        if get:
            kwargs.update({"data": get})
        return kwargs
