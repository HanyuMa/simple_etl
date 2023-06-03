from django.db import models


class UserExperimentCompound(models.Model):
    user_id = models.IntegerField(primary_key=True)
    total_experiments = models.IntegerField()
    total_run_time = models.IntegerField()
    average_experiments_amount = models.DecimalField(max_digits=100, decimal_places=2)
    mostly_used_compound = models.CharField(max_length=255)

    class Meta:
        db_table = "user_experiment_compound_data"


class CompoundCount(models.Model):
    compound_id = models.IntegerField(primary_key=True)
    compound_name = models.CharField(max_length=255)
    compound_count = models.IntegerField()

    class Meta:
        db_table = "compound_count_data"
