"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[i])):
            line += str(matrix[j][i]) + "\t"
        print(line)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    end = [] #temporarily hold the product, then will set m2 to this
    for c in range( len(m2[0]) ):#number of cols of end matrix is the number of cols in m2
        end.append( [] )
        for r in range( len(m1) ):#number of rows of end matrix is the number of rows in m1
            end[c].append( 0 )
    print_matrix(end) #*************************************************FOR TESTING*****

    # 
    # sum = 0
    # for r in range(len(m2)):
    #     sum += m1[]





def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
