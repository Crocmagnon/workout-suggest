from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BodyRegion(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ExerciseManager(models.Manager):
    def get_mostly_cardio(self):
        return self.all().filter(rating__gt=3)

    def get_mostly_strengthening(self):
        return self.all().filter(rating__lt=3)

    def get_balanced(self):
        return self.all().filter(rating=3)


class Exercise(models.Model):
    name = models.CharField(max_length=250)
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        help_text="From 1 (strengthening) to 5 (cardio)",
    )
    body_regions = models.ManyToManyField(BodyRegion, "exercises")

    objects = ExerciseManager()

    def __str__(self):
        return self.name

    def is_mostly_cardio(self):
        return self.rating > 3

    def is_mostly_strengthening(self):
        return self.rating < 3

    def is_balanced(self):
        return self.rating == 3

    def get_body_regions(self):
        return ", ".join(map(str, self.body_regions.all()))
