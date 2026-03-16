import numpy as alice
def alldgmtrx(alpha,beta):
    daplha=alice.diag(alpha)
    dbeta=alice.diag(beta)
    change=dalpha*dbeta
    afterchange=alice.diag(change)
    return afterchange
aplha=alice.array([3,0,0],
                                  [0,2,0],
                                  [0,0,1])
beta=alice.array([2,0,0],
                                [0,3,0],
                                [0,0,4])
result=alldgmtrx(alpha,beta)
print("MATRIX1:",alpha)
print("MATRIX2:",beta)
print("RESULT OF THE MULTIPLIED DIAGONAL MATRIX:",result)


