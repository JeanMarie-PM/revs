from django.db import models

# from django_model_history_tracker.mixins import HistoryTrackerMixin


class Reporter(
    models.Model
    #  , HistoryTrackerMixin
):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
