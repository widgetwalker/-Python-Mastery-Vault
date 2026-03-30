import numpy as np

def alldgmtrx(alpha, beta):
    dalpha = np.diag(alpha)
    dbeta = np.diag(beta)
    change = np.dot(dalpha, dbeta)
    afterchange = np.diag(change)
    return afterchange

alpha = np.array([3, 0, 0])
beta = np.array([2, 0, 0])

result = alldgmtrx(alpha, beta)

print("MATRIX1:")
print(np.diag(alpha))
print("\nMATRIX2:")
print(np.diag(beta))
print("\nRESULT OF THE MULTIPLIED DIAGONAL MATRIX:")
print(result)