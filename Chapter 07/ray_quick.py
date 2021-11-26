import ray
from ray import serve

from fastapi import FastAPI

app = FastAPI()

serve_handle = None

def say_hello(request):
    return "hello " + "request.name" + "!"

@app.on_event("startup") # Code to be run when the server starts.
async def startup_event():
    ray.init(address="auto") # Connect to the running Ray cluster.
    client = serve.start() # Start the Ray Serve client.

    client.create_backend("my_backend", say_hello)
    client.create_endpoint("my_endpoint", backend="my_backend")

    global serve_handle
    serve_handle = client.get_handle("my_endpoint")

@app.get("/predict")
async def predict(name: str):
        return await serve_handle.remote(name)