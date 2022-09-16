def printmatrix(A):
    for i in range(len(A)):
        print(A[i])
print('Enter the dimension of matrix 1:')
r1=int(input('Enter no of rows:'))
c1=int(input('Enter no of columns:'))
M=[]
for i in range(r1):
    print('Enter element of row-',i)
    C=[]
    for j in range(c1):
        n=int(input('Enter no:'))
        C.append(n)
    M.append(C)
print('The entered Matrix M is:')
printmatrix(M)
print('Enter the dimension of matrix 2:')
r2=int(input('Enter no of rows:'))
c2=int(input('Enter no of columns:'))
N=[]
for i in range(r2):
    print('Enter element of row-',i)
    D=[]
    for j in range(c2):
        m=int(input('Enter no:'))
        D.append(m)
    N.append(D)
print('The entered Matrix M2 is:')
printmatrix(N)
def matrixmul(A,B):
    C=[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))
       for i in range(len(A))]
    print('Multiplication of 2 matrices=')
    printmatrix(C)
if c1==r2:
    matrixmul(M,N)
else:
    print('Invalid Matrix :-To multiply 2 matrices matrix1 column=matrix2rows')
       
