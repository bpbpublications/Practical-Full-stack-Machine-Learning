import os
import sys
import click

import mlflow

@click.command()
@click.option("--max-iter", default=10, type=int)
@click.option("--keras-units", default=20, type=int)
def workflow(max_iter, keras_units):

    with mlflow.start_run() as active_run:
        #print(f"Parameters are max_iter={max_iter} and keras_units={keras_units}")

        print("Launching 'download'\n")
        download_run = mlflow.run(".", "download_data", parameters={})
        download_run = mlflow.tracking.MlflowClient().get_run(download_run.run_id)
        file_path_uri = os.path.join(download_run.info.artifact_uri, "data")
        print(f"The downloaded file URI is {file_path_uri}")


        print("Launching 'train'\n")
        train_run = mlflow.run(".", "train_data", parameters={"data_path": file_path_uri})
        train_run = mlflow.tracking.MlflowClient().get_run(train_run.run_id)
        data_path_uri = os.path.join(download_run.info.artifact_uri, "data","features.txt")
    
        print(f"Training the model with - {data_path_uri}")

if __name__ == "__main__":
    workflow()

