from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 255 ]
matrix = new_matrix()

m1 = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
m2 = []
print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)
print("\n")

print("Testing ident. m1 =")
ident(m1)
print_matrix(m1)
print("\n")

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)
print("\n")


print("Testing Matrix mult. m1 =")
m1 = [[1,2,3,1], [4,5,6,1], [7,8,9,1], [10,11,12,1]]
print_matrix(m1)
print("\n")

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)
print("\n")

#
# x = 0
# y = 500
# for i in range(10):
#     add_edge(matrix, x, y, 0, x + 100, y, 0)
#     add_edge(matrix, x + 100, y, 0, x + 100, y + 100, 0)
#     add_edge(matrix, x + 100, y + 100, 0, x, y + 100, 0)
#     add_edge(matrix, x, y + 100, 0, x, y, 0)
#
#     x += 50
#     y -= 50
#
# x = 0
# y = 250
# for i in range(10):
#     add_edge(matrix, x, y, 0, x + 100, y, 0)
#     add_edge(matrix, x + 100, y, 0, x + 100, y + 100, 0)
#     add_edge(matrix, x + 100, y + 100, 0, x, y + 100, 0)
#     add_edge(matrix, x, y + 100, 0, x, y, 0)
#
#     x += 50
#     y -= 50
#
# x = 200
# y = 500
# for i in range(10):
#     add_edge(matrix, x, y, 0, x + 100, y, 0)
#     add_edge(matrix, x + 100, y, 0, x + 100, y + 100, 0)
#     add_edge(matrix, x + 100, y + 100, 0, x, y + 100, 0)
#     add_edge(matrix, x, y + 100, 0, x, y, 0)
#
#     x += 50
#     y -= 50

#
# x = 0
# y = 0
# for i in range(5):
#     add_edge(matrix, x, y, 0, x + 100, y, 0)
#     add_edge(matrix, x + 100, y, 0 , x + 50, y + 50, 0)
#     add_edge(matrix, x + 50, y + 50, 0 , x, y, 0)
#
#     x += 100

# for i in range(10,50):
#     for j in range(150,175):
#         add_edge(matrix, i * j, i / j, 0, i % j, i + j, 0)

for i in range(0,300):
    add_edge(matrix, i + 350, i % 500, 0, i % 500, i + 20, 0)





draw_lines( matrix, screen, color )
display(screen)
