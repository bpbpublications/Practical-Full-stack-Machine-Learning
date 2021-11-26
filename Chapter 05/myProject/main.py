import mlflow
import warnings
import sys


if __name__ == '__main__':
    # suppress any deprcated warnings
    # warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Extract the command line parameter lambda
    mY_lambda = float(sys.argv[1])

    parameters = [{'alpha': 0.3, 'lambda':mY_lambda},
                 {'alpha': 0.4, 'lambda':mY_lambda},
                 {'alpha': 0.5, 'lambda':mY_lambda}]
    
    

   # Iterate over three different runs with different parameters
    for param in parameters:
      print(f"Running with param = {param}")