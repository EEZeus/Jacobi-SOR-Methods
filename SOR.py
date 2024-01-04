## Ehsan Espandar - 99442011 - Jacobi Method for N*N A matrix

import numpy as np
from numpy import linalg


## Selecting Arbitrary Ab,epsilon, and X_0
## Attention A must be 3-diagonal and Determined Positive

Ab = np.array([[5, 2, 0, 29],
               [2, 5, 2, 33],
               [0, 2, 1, 10]], dtype=float)
X_0 = np.zeros(len(Ab))
epsilon = 0.0005


print("Updated Ab:")
print(Ab)

## Separating A and b from Ab
A = Ab[:, :-1]
b = Ab[:, -1]

print(A,b)
## Calculating optimum omega

temp = -1 / np.diag(A)
minesDinverse = np.diag(temp)
LplusU = A - np.diag(np.diag(A))
Hj = np.matmul(minesDinverse, LplusU)
values, vectors = np.linalg.eig(Hj)
Ro = np.max(np.abs(values))
omega = 2 / (1 + np.sqrt(1 - Ro**2))

print('=====================\n','Omega :',omega,'\n====================\n')


## Implementing SOR Algorithm 
def SOR(A, b, omega, X_0, epsilon):
    step = 0
    phi = X_0.copy()
    err = linalg.norm(A @ phi - b)  
    while err > epsilon:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i, j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
        err = linalg.norm(A @ phi - b)
        step += 1
        print('=====================\n',"Step {} X is :".format(step),phi)
        print("Step {} Error: {:10.6g}".format(step, err))
    return phi


X = SOR(A, b, omega, X_0, epsilon)
print('X is :',X)

