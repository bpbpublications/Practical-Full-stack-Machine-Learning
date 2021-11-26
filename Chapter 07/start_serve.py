import ray
from ray import serve
ray.init(address='auto') # Connect to the running Ray cluster.