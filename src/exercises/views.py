from django.views import generic

from exercises.models import Exercise


class RandomExercisesView(generic.ListView):
    model = Exercise
    context_object_name = "exercises"

    def get_queryset(self):
        return Exercise.objects.order_by("?")[:5]
