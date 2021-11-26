from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Loading Iris Dataset
iris = load_iris()

for keys in iris.keys() :
    print(keys)

# Getting features and targets from the dataset
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5)

print(X_train.shape)
print(X_test.shape)

logreg=LogisticRegression(solver='lbfgs', multi_class='auto')

# Fitting our Model on the dataset
logreg.fit(X_train,y_train)

X_new=[[4.4,3.2,1.3,0.2]]
y_pred=logreg.predict(X_new)
print(y_pred)

y_pred = logreg.predict(X_test)

print(logreg.score(X_test, y_test))

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

@app.get("/")
def home_page():
    return {"Hello": "World"}

@app.post("/predict")
def predict(data : request_body):
    test_data = [[
            data.sepal_length, 
            data.sepal_width, 
            data.petal_length, 
            data.petal_width
    ]]
    class_idx = logreg.predict(test_data)[0]
    return { 'class' : iris.target_names[class_idx]}