# The name of the database is `simple_etl_db_1` and the name of the table is `user_experiment_compound_data`.
docker exec -it simple_etl_db_1 psql -U postgres -d postgres -c "SELECT * FROM user_experiment_compound_data"