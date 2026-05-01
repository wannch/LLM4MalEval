import numpy as np
def euclidean_distance(X1:np.ndarray,X2:np.ndarray):
  X1=np.expand_dims(X1,axis=2)
  X2=np.expand_dims(X2.T,axis=0)
  dist=np.sqrt(np.sum((X2-X1)**2,axis=1))
  return dist
