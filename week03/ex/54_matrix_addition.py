import numpy as np
def matrix_addition(matrix1,matrix2):
    sum=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum[i][j]=matrix1[i][j]+matrix2[i][j]
    sum_matrix=np.array(sum)
    print("Matrix1:\n",str(matrix1).replace("[","").replace("]","").replace(",",""))
    print("Matrix2:\n",str(matrix2).replace("[","").replace("]","").replace(",",""))
    print("The result of matrix is:\n",str(sum_matrix).replace("[","").replace("]","").replace(",",""))
matrix1=np.array([[10,5,4,2],[5,0,9,5],[9,19,60,8],[7,8,4,5]])
matrix2=np.array([[12,65,34,42],[10,5,89,45],[11,21,63,78],[87,78,54,65]])
matrix_addition(matrix1,matrix2)



