#!/usr/bin/python


def poly(n):
    
    return(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10)

    ## return (1 -n*(1+n*(1-n*(1+n*(1-n*(1+n*(1-n*(1+n*(1-n*(1L+n))))))))))
def gauss(AMatrix, BMatrix):

   # solve linear equations of the form:
   #     |A00 A01 ... A0n|   |coefficient0|   |B0|
   #     |A10 A11 ... A1n| * |coefficient1| = |B1|
   #     |... ... ... ...|   |     ...    |   |..|
   #     |An0 An1 ... Ann|   |coefficientn|   |Bn|
   # where |A| and |B| are supplied and |coefficient| is the solution.

   # require part of contract

   # get the length of the matrix
   n = len(AMatrix)

   # copy the matrices to local variables - inplace substitution used
   A = map(lambda x: list(x), AMatrix)
   B = list(BMatrix)

   # initialize the output results
   coefficients = [0] * n

   # condition the matrix for the solution
   for i in range(n-1):
      pivot = A[i][i]
      assert(pivot != 0), \
         "Zero pivot value encountered"
      for j in range(i+1, n):
         multiplier = float(A[j][i]) / pivot
         for k in range(i+1, n):
            A[j][k] = A[j][k] - multiplier * A[i][k]
         B[j] = B[j] - multiplier * B[i]

   # solve for the coefficients
   assert(A[n-1][n-1] != 0), \
      "Divide by zero encountered in solution"
   coefficients[n-1] = float(B[n-1]) / A[n-1][n-1]
   for i in range(n-2, -1, -1):
      top = B[i]
      for j in range(i+1, n):
         top = top - (A[i][j]* coefficients[j])
      assert(A[i][i] != 0), \
         "Divide by zero encountered in solution"
      coefficients[i] = float(top) / A[i][i]

   return coefficients

def poly_coef(coefs,n):
    res=0
    for i in range(len(coefs)):
        res+=coefs[i]*(n**i)
    return res
def make_matrix(rang):
    res=[]
    for i in range(1,rang+1):
        tmp=[1]
        for j in range(rang-1):
            tmp.append(tmp[-1]*i)
        res.append(tmp)
    return res
if __name__=='__main__':
    ## print make_matrix(5)
    resultat=0
    for rang in range(1,11):
        
        amatrix=make_matrix(rang)

        bmatrix=[]
        for i in range(1,rang+1):
        ##  bmatrix.append(i*i*i)
            bmatrix.append(poly(i))
        print bmatrix
        res=gauss(amatrix,bmatrix)
        tmp=poly_coef(res,rang+1)
        resultat +=tmp 
    print "###  resultat:%s"%(resultat,)
