import pandas as pd
from django.conf import settings
from simple_etl.models import UserExperimentCompound


def etl():
    # Load CSV files
    users_file = "data/users.csv"
    user_experiments_file = "data/user_experiments.csv"
    compounds_file = "data/compounds.csv"
    # Read the CSV file with comma (',') as the delimiter. Remove tabs from values.
    users_df = pd.read_csv(users_file).replace("\t", "", regex=True)
    user_experiments_df = pd.read_csv(user_experiments_file).replace(
        "\t", "", regex=True
    )
    compounds_df = pd.read_csv(compounds_file).replace("\t", "", regex=True)
    # Remove tabs from column names
    users_df.columns = users_df.columns.str.replace("\t", "")
    user_experiments_df.columns = user_experiments_df.columns.str.replace("\t", "")
    compounds_df.columns = compounds_df.columns.str.replace("\t", "")

    # Process files to derive features
    # Calculate the total number of experiments per user
    total_experiments = (
        user_experiments_df.groupby("user_id")
        .size()
        .reset_index(name="total_experiments")
    )

    # Calculate the total run time per user
    total_run_time = (
        user_experiments_df.groupby("user_id")["experiment_run_time"]
        .sum()
        .reset_index(name="total_run_time")
    )

    # Calculate the average run time per experiment
    average_run_time = pd.merge(total_experiments, total_run_time, on="user_id")
    average_run_time["average_run_time"] = (
        average_run_time["total_run_time"] / average_run_time["total_experiments"]
    )

    # Split and explode the compound IDs for each user
    user_experiments_df["experiment_compound_ids"] = user_experiments_df[
        "experiment_compound_ids"
    ].str.split(";")
    user_experiments_df = user_experiments_df.explode("experiment_compound_ids")
    user_experiments_df["experiment_compound_ids"] = user_experiments_df[
        "experiment_compound_ids"
    ].astype(int)

    # Calculate the count of each compound used by each user
    compound_counts = (
        user_experiments_df.groupby(["user_id", "experiment_compound_ids"])
        .size()
        .reset_index(name="count")
    )

    # Join the compounds_df with compound_counts to get compound names
    compound_counts = pd.merge(
        compound_counts,
        compounds_df[["compound_id", "compound_name"]],
        left_on="experiment_compound_ids",
        right_on="compound_id",
        how="left",
    )

    # Find the most commonly used compound for each user
    mostly_used_compound = (
        compound_counts.groupby("user_id")
        .apply(
            lambda x: ";".join(
                x[x["count"] == x["count"].max()]["compound_name"].astype(str)
            )
        )
        .reset_index(name="mostly_used_compound")
    )

    # Combine `average_run_time` and `mostly_used_compound` into one with user_id as the primary key
    combined_df = pd.merge(
        average_run_time, mostly_used_compound, on="user_id", how="outer"
    )

    # Convert the `combined_df` to the `UserExperimentCompound` model.
    for index, row in combined_df.iterrows():
        myModel = UserExperimentCompound(
            user_id=row["user_id"],
            total_experiments=row["total_experiments"],
            total_run_time=row["total_run_time"],
            average_experiments_amount=row["average_run_time"],
            mostly_used_compound=row["mostly_used_compound"],
        )
        # Upload processed data into a database
        myModel.save()


# Your API that can be called to trigger your ETL process
def trigger_etl():
    # Trigger your ETL process here
    etl()
    return {"message": "ETL process started"}, 200
