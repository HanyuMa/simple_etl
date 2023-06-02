# Generated by Django 4.0.10 on 2023-06-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserExperimentCompound',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('total_experiments', models.IntegerField()),
                ('total_run_time', models.IntegerField()),
                ('average_experiments_amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('mostly_used_compound', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user_experiment_compound_data',
            },
        ),
    ]
