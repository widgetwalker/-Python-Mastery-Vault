import numpy as np

def alldgmtrx(alpha, beta,gamma):
    dalpha = np.diag(alpha)
    dbeta = np.diag(beta)
    dgamma=np.diag(gamma)
    change = np.dot(dalpha, dbeta,dgamma)
    afterchange = np.diag(change)
    return afterchange

alpha = np.array([3, 0, 0])
beta = np.array([2, 0, 0])
gamma=np.array([1,0,0])

result = alldgmtrx(alpha, beta,gamma)

print("MATRIX1:")
print(alpha)
print("\nMATRIX2:")
print(beta)
print("\nMATRIX3:")
print(gamma)
print("\nRESULT OF THE MULTIPLIED DIAGONAL MATRIX:")
print(result)