# simple_etl

This repository contains an ETL (Extract, Transform, Load) application built with Python, Django and Docker. The application fetches data from the `data` folder, performs necessary transformations, and loads it into a PostgreSQL database.

## Why Django and how it works for this project
1. Django ships with built-in support for PostgreSQL and other databases. The actual Django code will be almost identical for different databases. We only need to update `DATABASE` settings in `django_project/settings.py` and install the desired database. Here, I use `psycopg2-binary` for PostgreSQL.

2. Django provides web services and makes it simple to create an API that accepts a POST request.

## Requirements

- Docker

## Getting Started

To get started with the ETL application, follow the steps below:

1. **Clone the repository**:

```bash
git clone https://github.com/HanyuMa/simple_etl.git
cd simple_etl
```

2. **Build and run the Docker container:**

```bash
chmod +x build_and_run.sh
./build_and_run.sh
```

This script will build the Docker image using the provided Dockerfile and start the container. It assumes you have Docker installed and running.

3. **Trigger the ETL process:**
```bash
chmod +x run_etl.sh
./run_etl.sh
```
This script uses curl to make an HTTP request to the API endpoint responsible for triggering the ETL process.

4. **Check the database:**
```bash
chmod +x query_database.sh
./query_database.sh
```
This script allows you to query the database to verify that it has been populated with the desired features.

5. **Turn off the Docker services**
```bash
docker-compose down
```

6. **Run unit tests**
Before turning of the Docker services, you can run the unit tests in `simple_etl/tests.py`:
```bash
docker exec -it simple_etl_web_1 python3 manage.py test
```

# Repository Structure
* Dockerfile: Defines the Docker image configuration for the application.
* requirements.txt: Lists all the Python dependencies required for the application.
* manage.py: Django management script for running various commands.
* docker-compose.yml: Define and manage multi-container Docker applications, i.e. web and db services.
* data: All CSV files to be processed.
* django_project: Setups of the Django project.
* simple_etl: The app of the Django project.
* build_and_run.sh: Script to build and run the Docker container.
* run_etl.sh: Script to trigger the ETL process.
* query_database.sh: Script to query the database and showcase populated features.

# Deliverables
1. Dockerfile
2. requirement.txt
3. simple_etl/etl_scripts.py: A Python script that runs the ETL process. simple_etl/views.py and simple_etl/urls.py sets up the API that accepts a POST request.
4. README
5. build_and_run.sh
6. run_etl.sh
7. query_database.sh