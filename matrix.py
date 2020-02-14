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
    rows = len(m1) #number of rows in the end product is the number of rows in m1
    cols = len(m2[0]) #number of cols in the end product is the number of cols in m2
    print("ROWS: " + str(rows))
    print("COLS: " + str(cols))

    #FIRST ROW * FIRST COL
    sum1 = 0
    for i in range(rows + 1):
        sum1 += m1[0][i] * m2[i][0]

    print("SUM1: " + str(sum1))

    #FIRST ROW * SECOND COL
    sum2 = 0
    for i in range(rows + 1):
        sum2 += m1[0][i] * m2[i][1]

    print("SUM2: " + str(sum2))

    #SECOND ROW * FIRST COL
    sum3 = 0
    for i in range(rows + 1):
        sum3 += m1[1][i] * m2[i][0]

    print("SUM3: " + str(sum3))

    #SECOND ROW * SECOND COL
    sum4 = 0
    for i in range(rows + 1):
        sum4 += m1[1][i] * m2[i][1]

    print("SUM4: " + str(sum4))

    for a in range(rows * cols):
        sum = 0
        for i in range(cols):
            for j in range(rows):
                if j >= rows and i >= cols:
                    sum += m1[j-1][i-1] * m2[i-1][j-1]
                elif j >= rows:
                    sum += m1[j-1][i] * m2[i][j-1]
                elif i >= cols:
                    sum += m1[j][i-1] * m2[i-1][j]
                else:
                    sum += m1[j][i] * m2[i][j]
        print(sum)






    # for a in range(rows * cols):
    #     sum = 0
    #     for i in range(rows + 1): #offset by 1
    #         for j in range(cols + 1):
    #             sum += m1[j][i] * m2[i][j]
    #     print(str(sum))





def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
