"""
Dummy python application mocking data download operation
"""
import os
import mlflow


def download_data():
    with mlflow.start_run() as mlrun:

        print("Downloading Data\n")

        #Create a features.txt artifact file
        features = "rooms, zipcode, median_price, school_rating, transport"
        
        with open("features.txt", 'w') as f:
            f.write(features)
        
        mlflow.log_artifact("features.txt","data")
    

if __name__ == "__main__":
    download_data()
