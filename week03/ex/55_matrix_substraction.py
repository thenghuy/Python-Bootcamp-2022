import numpy as np
def matrix_substraction(matrix1,matrix2):
    substract=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            substract[i][j]=matrix1[i][j]-matrix2[i][j]
    substract_matrix=np.array(substract)
    print("Matrix1:\n",str(matrix1).replace("[","").replace("]","").replace(",",""))
    print("\nMatrix2:\n",str(matrix2).replace("[","").replace("]","").replace(",",""))
    print("The result of matrix is:\n",str(substract_matrix).replace("[","").replace("]","").replace(",",""))
matrix1=np.array([[10,5,4,2],[5,10,9,55],[9,19,69,8],[7,8,4,75]])
matrix2=np.array([[12,65,34,2],[1,5,8,45],[7,21,63,8],[0,78,4,65]])
matrix_substraction(matrix1,matrix2)