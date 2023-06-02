from django.test import TestCase
from .models import UserExperimentCompound


class SimpleEtlTests(TestCase):
    # Test url exist at correct location
    def test_trigger_etl_url_exists_at_desired_location(self):
        response = self.client.get("/trigger-etl/")
        self.assertEqual(response.status_code, 200)

    # Trigger the ETL process and test if the table is populated
    def test_etl_produce_a_table(self):
        # Trigger the ETL process
        self.client.get("/trigger-etl/")

        # Check if the table is created and populated
        self.assertEqual(UserExperimentCompound.objects.count(), 10)

    # Trigger the ETL process and test if the values are correct
    def test_etl_produce_correct_values(self):
        # Trigger the ETL process
        self.client.get("/trigger-etl/")
        # Check if the table is correctly populated
        # Check the results for user_id=1. The values should be:
        # total_experiments=2, total_run_time=25, average_experiments_amount=12.50, mostly_used_compound="2"
        user_experiment_compound = UserExperimentCompound.objects.get(user_id=1)
        self.assertEqual(user_experiment_compound.total_experiments, 2)
        self.assertEqual(user_experiment_compound.total_run_time, 25)
        self.assertEqual(user_experiment_compound.average_experiments_amount, 12.50)
        self.assertEqual(user_experiment_compound.mostly_used_compound, "2")

        # Check the results for user_id=4. The values should be:
        # total_experiments=1, total_run_time=30, average_experiments_amount=30.00, mostly_used_compound="1;2;3"
        user_experiment_compound = UserExperimentCompound.objects.get(user_id=4)
        self.assertEqual(user_experiment_compound.total_experiments, 1)
        self.assertEqual(user_experiment_compound.total_run_time, 30)
        self.assertEqual(user_experiment_compound.average_experiments_amount, 30.00)
        self.assertEqual(user_experiment_compound.mostly_used_compound, "1;2;3")
