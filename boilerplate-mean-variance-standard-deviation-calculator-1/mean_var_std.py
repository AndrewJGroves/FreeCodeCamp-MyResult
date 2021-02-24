import numpy as np

def calculate(list):
  try:
    new = np.array(list).reshape(3,3)
  except :
    raise ValueError("List must contain nine numbers.")


  calc= {
    "mean": [new.mean(axis=0).tolist(),new.mean(axis=1).tolist(),new.mean()],
    "variance":[new.var(axis=0).tolist(),new.var(axis=1).tolist(),new.var()],
    "standard deviation":[new.std(axis=0).tolist(),new.std(axis=1).tolist(),new.std()],
    "max":[new.max(axis=0).tolist(),new.max(axis=1).tolist(),new.max()],
    "min":[new.min(axis=0).tolist(),new.min(axis=1).tolist(),new.min()],
    "sum":[new.sum(axis=0).tolist(),new.sum(axis=1).tolist(),new.sum()]
  }

  return calc
