import numpy as np
A = np.array([[3,5,6],[4,8,10],[2,1,8]])
I = np.array([[1,0,0],[0,1,0],[0,0,1]])
M=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        for k in range(3):
            M[i][j]+=A[i][k]*I[k][j]
print(M)
if(np.array_equal(A,M)):
    print("It is equal. Hence Proved!!!")
else:
    print("Not Equal")
