import os
import mlflow
import click

@click.command()
@click.option("--data-path", default="features.txt")
def train_data(data_path):
    
    with mlflow.start_run() as mlrun:
        
        print("training features = : %s" % data_path)

        # As a dummy transformation, let us rename the txt file
        artifact_uri = mlflow.get_artifact_uri(artifact_path=data_path)
        
        print("Artifact uri for training data : {}".format(artifact_uri))
                

if __name__ == "__main__":
    train_data()
