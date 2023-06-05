from django.test import TestCase
from .models import UserExperimentCompound, CompoundCount


class SimpleEtlTests(TestCase):
    # Test url exist at correct location
    def test_trigger_etl_url_exists_at_desired_location(self):
        response = self.client.get("/trigger-etl/")
        self.assertEqual(response.status_code, 200)

    # Trigger the ETL process and test if the table is populated
    def test_etl_produces_a_table(self):
        # Trigger the ETL process
        self.client.get("/trigger-etl/")

        # Check if the table is created and populated
        self.assertEqual(UserExperimentCompound.objects.count(), 10)
        # Check the count in the compound_count_data table
        self.assertEqual(CompoundCount.objects.count(), 3)

    # Trigger the ETL process and test if the values are correct
    def test_etl_produces_correct_values(self):
        # Trigger the ETL process
        self.client.get("/trigger-etl/")
        # Check if the table is correctly populated
        # Check the results for user_id=1. The values should be:
        # total_experiments=2, total_run_time=25, average_experiments_amount=12.50, mostly_used_compound="Compound B"
        user_experiment_compound = UserExperimentCompound.objects.get(user_id=1)
        self.assertEqual(user_experiment_compound.total_experiments, 2)
        self.assertEqual(user_experiment_compound.total_run_time, 25)
        self.assertEqual(user_experiment_compound.average_experiments_amount, 12.50)
        self.assertEqual(user_experiment_compound.mostly_used_compound, "Compound B")

        # Check the results for user_id=4. The values should be:
        # total_experiments=1, total_run_time=30, average_experiments_amount=30.00, mostly_used_compound="Compound A;Compound B;Compound C"
        user_experiment_compound = UserExperimentCompound.objects.get(user_id=4)
        self.assertEqual(user_experiment_compound.total_experiments, 1)
        self.assertEqual(user_experiment_compound.total_run_time, 30)
        self.assertEqual(user_experiment_compound.average_experiments_amount, 30.00)
        self.assertEqual(
            user_experiment_compound.mostly_used_compound,
            "Compound A;Compound B;Compound C",
        )

        # Check the number of count for Compound A. The value should be 6.
        compound_count = CompoundCount.objects.get(compound_id=1)
        self.assertEqual(compound_count.compound_count, 6)

        # Check the number of count for Compound B. The value should be 8.
        compound_count = CompoundCount.objects.get(compound_id=2)
        self.assertEqual(compound_count.compound_count, 8)

        # Check the number of count for Compound C. The value should be 9.
        compound_count = CompoundCount.objects.get(compound_id=3)
        self.assertEqual(compound_count.compound_count, 9)
