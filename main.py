from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

matrix[0] = ["x0", "y0", "z0", 1]
matrix[1] = ["x1", "y1", "z1", 1]
matrix[2] = ["x2", "y2", "z2", 1]
matrix[3] = ["x3", "y3", "z3", 1]


print_matrix(matrix)
print("\n")
ident(matrix)
print_matrix(matrix)


#
# draw_lines( matrix, screen, color )
# display(screen)
