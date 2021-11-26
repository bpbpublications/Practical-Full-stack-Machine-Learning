import mlflow.pyfunc
import mlflow
import pandas as pd
mlflow.set_tracking_uri("http://localhost:5000")

model_name = "estimator1"
stage = 'Production'

model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}/{stage}"
)
input_sample = {'x1': [3.0, 2.0], 'x2': [2.5,3.8]}
df = pd.DataFrame.from_dict(input_sample)

print(model.predict(df))
