import numpy

A = numpy.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
Y = numpy.array([-4,3,9,7],float)
#SOLVES A*X = Y for X.
#input is a square matrix, A, which has no leading zeros, that is, no element of
#the first column can have a zero value and Value matrix, Y, from which we use to find X vector
#It does this by Guassian elimination, iterating such that multiples of the 1st row are
#deducted from 2nd, 3rd.... to achieve trail of zeros in 1st column except at A[0,0] which is 1
#the move to next column and repeat but minus multiples of 2nd row from 3rd, 4th ...row.
#Result is a diagonal matrix with lower trianguler portion bieng zeros and a leading diagonal
#of 1's. The uses backward substitution to determine the values of X vector.

#A must be a square matrix(M,N) and Y a column vector of length M 

#first Diagonalize the matrix A

def Diagonalize(A,Y):
    M,N = numpy.shape(A)
    for m in range(M):                                
        divisor = A[m,m]                    
        A[m,:] /= divisor                   
        Y[m]   /= divisor
        for n in range(m+1,N):              
            multiplier = A[n,m]
            A[n,:]    -= multiplier*A[m,:]
            Y[n]      -= multiplier*Y[m]
    return A

#then use backwards substitution to determine each value of the X vector, once
#the matrix A is diagonalized

def Backwards_Sub(A,Y):
    M,N = numpy.shape(A)
    X   = numpy.empty(M,float)
    for m in range(M-1,-1,-1):
        X[m]= Y[m]
        for n in range(m+1,N):
            X[m] -=A[m,n]*X[n]
    return X

#combine both user functions to solve for X

def Square_Matrix_Solver(A,Y):
    diagonal = Diagonalize(A,Y)
    X_Vector = Backwards_Sub(diagonal,Y)
    return X_Vector

            



