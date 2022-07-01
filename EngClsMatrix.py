###############################################################################################################################################################
#
# Módulo : ENG Classe Matrix               Data de Criação: 02/06/2022
#
# Objetivo: Módulo para representação de uma matriz e suas propriedades: Criação de Matriz, Operações Matriciais, Inversa, entre outras.
#
# Ultimas alterações: Criação
#
# Data da ultima alteração: 01/06/2022
#
# Desenvolvedor: Francisco J. E. de Sousa
#
# Contato: e-mail: francisco.sousa1993@outlook.com      tel: (21) 96965-6759
#
###############################################################################################################################################################

# Imports:

import numpy as np
import EngClsDataFrame as eDf
from EngConstants import *

# Class #1:
class EngClsMatrixOperation(object):

    def __ini__(self,dbType=eDf.ENG_DBTYPE_CSV):
        self.manageData=eDf.DataBaseSource(dbType)

    def CalcInverse(self,matrix):
        return np.linalg.inv(matrix)

    def ScalarProduct(self,matrix, scalar):
        return matrix*scalar

    def VetorialProduct(self,matrixA,matrixB):
        return np.inner(matrixA,matrixB)

    def Determinant(self,matrixA):
        return np.linalg.det(matrixA)

    def Identity(self,order):
        return np.identity(order)

    def Transpose(self,matrix):
        return matrix.transpose()

# Class #2:
class CalcTrendPolinomial(object):
    def __init__(self):
        return

    def CalcMatrixA(self,data,degree):
        dimension=degree+1
        matrix=np.identity(dimension)
        for i in range(dimension):
            for j in range(dimension):
                sum=0
                for element in data:
                    sum+=element**(i+j)
                matrix[dimension-i-1,dimension-j-1]=sum
        return matrix

    def CalcMatrixB(self,dataX,dataY,degree):
        dimension=degree+1
        matrix=[]        
        for i in range(dimension):
            sum=0
            for x,y in zip(dataX,dataY):
                sum+=y*(x**(dimension-i-1))
            matrix.append(sum)
        return np.array(matrix)

    def CalcMatrixX(self,matrixA,MatrixB):
        emo=EngClsMatrixOperation()
        invA=emo.CalcInverse(matrixA)
        return invA.dot(np.vstack(MatrixB))

    def CalcCoefficients(self,dataX,dataY,degree):
        A=self.CalcMatrixA(dataX,degree)
        B=self.CalcMatrixB(dataX,dataY,degree)
        return self.CalcMatrixX(A,B)

