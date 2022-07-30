import numpy as np
def matrix_multiplication(matrix1,matrix2):
    multi=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(matrix1)):
        # row of matix2 = column matrix 1
         for j in range(len(matrix2)):
            # column of matrix 2
            for k in range(len(matrix2[0])):
                multi[i][k] += matrix1[i][j] * matrix2[j][k]
    sum_matrix=np.array(multi)
    print("Matrix1:\n",str(matrix1).replace("[","").replace("]","").replace(",",""))
    print("Matrix2:\n",str(matrix2).replace("[","").replace("]","").replace(",",""))
    print("The result of matrix is:\n",str(sum_matrix).replace("[","").replace("]","").replace(",",""))
matrix1=np.array([[3,7,5],[2,6,7],[4,3,2]])
matrix2=np.array([[6,5,4],[3,2,1],[1,2,3]])
matrix_multiplication(matrix1,matrix2)