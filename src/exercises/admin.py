from django.contrib import admin
from django.contrib.admin import register

from exercises.models import BodyRegion, Exercise


@register(BodyRegion)
class BodyRegionAdmin(admin.ModelAdmin):
    list_display = ["name"]


@register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["name", "get_body_regions", "rating"]
    list_filter = ["body_regions", "rating"]
    search_fields = ["name"]
