import numpy as np
import scipy
import scipy.linalg as LA

A = np.array([[1,0,1],

print(A.T@A) #A.T is A transpose and @ means matrix multiplication

G = np.linalg.cholesky(A.T@A) #G ends up being lower triangular
