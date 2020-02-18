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
    xCors = ""
    yCors = ""
    zCors = ""
    nums = ""
    for i in range(len(matrix)):
        xCors += str(matrix[i][0]) + "\t"
        yCors += str(matrix[i][1]) + "\t"
        zCors += str(matrix[i][2]) + "\t"
        nums += str(matrix[i][3]) + "\t"
    print(xCors)
    print(yCors)
    print(zCors)
    print(nums)

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
    temp = new_matrix(cols = len(m2))
    for r in range(len(m2)):
        for c in range(len(m1[0])):
            for x in range(len(m1)):
                temp[r][c] += m2[r][x] * m1[x][c]
    for r in range(len(temp)):
        for c in range(len(temp[0])):
            m2[r][c] = temp[r][c]


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
