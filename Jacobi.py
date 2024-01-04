## Ehsan Espandar - 99442011 - Jacobi Method for N*N A matrix
import numpy as np

## Selecting Arbitrary Ab,epsilon, and X_0

Ab = [
 [-1,1,7,-6],
  [4,-1,-1,3],
  [-2,6,1,9]
]
X_0 = np.zeros(len(Ab))
epsilon = 0.0005

## Initializing variables

A = []
b = []
err = []
X_k = []
X_kPlusOne = []
k = 1

## Convert Ab into Diagonal Dominant Form
for i in range(len(Ab)):
    for j in range(len(Ab[i]) - 1):
        if Ab[i][i] < Ab[i][j]:
            temp = Ab[i]
            Ab[i] = Ab[j]
            Ab[j] = temp

## Separating A from Ab
for i in range(len(Ab)):
    A.append([])
    for j in range(len(Ab[i]) - 1):
        A[i].append(Ab[i][j])

## Separating b from Ab
for i in range(len(Ab)):
    b.append(Ab[i][-1])


## Initializing X_k as X_0 for first step
for i in range(len(A)):
    X_k.append(X_0[i])


## Jacobi Iteration formula Implementation:
## Xi_(k+1) = bi-sum(A[i][j] where i!=j) / A[i][i]

while True:
    sum_val = 0
    err = []
    for i in range(len(A)):
        sum_val = 0
        for j in range(len(A[i])):
            if i != j:
                sum_val += A[i][j] * X_k[j]

        X_kPlusOne.append((b[i] - sum_val) / A[i][i])

    for i in range(len(X_k)):
        err.append(X_kPlusOne[i] - X_k[i])

    for i in range(len(X_k)):
        X_k[i] = X_kPlusOne[i]

    X_kPlusOne = []

## Printing X vector in each step
    print(f"Step {k} :\n")
    for i in range(len(X_k)):
        print(f"X_{i+1} = {X_k[i]} ,")

    print("=========================\n")
    k += 1
    if abs(max(err)) < epsilon:
        break
