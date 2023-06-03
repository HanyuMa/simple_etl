# The name of the database is `simple_etl_db_1` and the name of the table is `user_experiment_compound_data`.
echo The PostgreSQL table is as below:
docker exec -it simple_etl_db_1 psql -U postgres -d postgres -c "SELECT * FROM user_experiment_compound_data"

# The average number of experiments among all users. Calculated as the sum of `total_experiments` divided by the number of unique users.
echo The average number of experiments per user among all users is:
docker exec -it simple_etl_db_1 psql -U postgres -d postgres -t -c "SELECT SUM(total_experiments)::decimal/COUNT(DISTINCT user_id) FROM user_experiment_compound_data"

# The mostly used compound among all users. Calculated as the compound with the highest number of experiments.
# This number is calculated with table compound_count_data.
echo The mostly used compound among all users is:
docker exec -it simple_etl_db_1 psql -U postgres -d postgres -c "SELECT compound_name, compound_count FROM compound_count_data WHERE compound_count = (SELECT MAX(compound_count) FROM compound_count_data)"