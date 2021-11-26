import ray
from ray import serve
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

from fastapi import FastAPI, Request
from pydantic import BaseModel
app = FastAPI()

serve_handle = None

@app.on_event("startup")  # Code to be run when the server starts.
async def startup_event():
    ray.init(address="auto") # Connect to the running Ray cluster.
    client = serve.start() # Start the Ray Serve client.

    class sklean_LRModel:
        def __init__(self) -> None:
            self.iris = load_iris()
            X = self.iris.data
            y = self.iris.target

            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5)

            self.logreg=LogisticRegression(solver='lbfgs', multi_class='auto')

            # Fitting our Model on the dataset
            self.logreg.fit(X_train,y_train)

        async def __call__(self, request):
            payload = request
            input_vector = [[
            payload._data.sepal_length, 
            payload._data.sepal_width, 
            payload._data.petal_length, 
            payload._data.petal_width
            ]]
            
            class_idx = self.logreg.predict(input_vector)[0]
            return { 'class' : self.iris.target_names[class_idx]}
            

    client.create_backend("sklean_LRModel_backend", sklean_LRModel)
    client.create_endpoint("iris_classifier", backend="sklean_LRModel_backend")

    global serve_handle
    serve_handle = client.get_handle("iris_classifier")

class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

@app.post("/predict")
async def predict(data: request_body):
    return await serve_handle.remote(data)       
