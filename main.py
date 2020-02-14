from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

# matrix[0] = ["x0", "y0", "z0", 1]
# matrix[1] = ["x1", "y1", "z1", 1]
# matrix[2] = ["x2", "y2", "z2", 1]
# matrix[3] = ["x3", "y3", "z3", 1]


#testing print_matrix and ident
# print_matrix(matrix)
# print("\n")
# ident(matrix)
# print_matrix(matrix)
# print("\n")

#testing print_matrix for non-square matricies
# test = [
#     ["x0", "y0", "z0", 1],
#     ["x1", "y1", "z1", 1],
#     ["x2", "y2", "z2", 1],
#     ["x3", "y3", "z3", 1],
#     ["x4", "y4", "z4", 1],
#     ["x5", "y5", "z5", 1],
#     ["x6", "y6", "z6", 1],
#     ["x7", "y7", "z7", 1],
# ]
# print_matrix(test)





m1 = [
    [1, 2, 3],
    [4, 5, 6]
    ]

m2 = [
    [7, 8],
    [9, 10],
    [11, 12]
    ]

matrix_mult(m1, m2)




# draw_lines( matrix, screen, color )
# display(screen)
