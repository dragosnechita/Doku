from functions import print_table
from math import floor
sudoku = []

"""used to see the whole sudoku layout"""
for item in range(81):
  sudoku.append(item)
print_table(sudoku)

h_line_list = []
def h_line_generator(h_line):
    """used to generate a horizontal line to check whether the current cell value respects 
    the principles of Sudoku"""
    for cell in range(line * 9, line * 9 + 9):
        h_line.append(sudoku[cell])
v_line_list = []
def v_line_generator(v_line):
    """used to generate a vertical line to check whether the current cell value respects 
    the principles of Sudoku"""
    for cell in range(line, 80, 9):
        v_line.append(sudoku[cell])
cluster_list = []
def cluster_generator(cluster):
    """used to generate a cluster of 3by3 cells to check whether the current cell value respects 
    the principles of Sudoku"""
    for cell in range(cluster, cluster + 3):
        cluster.append(sudoku[cell])
    for cell in range(cluster + 9, cluster + 12):
        cluster.append(sudoku[cell])
    for cell in range(cluster + 18 , cluster + 21):
        cluster.append(sudoku[cell])

def h_line_define(cell):
    """used to find out which h line should be generated to check sudoku rules"""
    h_line = floor(cell / 9)
    return h_line

def v_line_define(cell):
    """used to find out which v line should be generated to check sudoku rules"""
    v_line = cell % 9
    return v_line

def cluster_define(cell):
    if cell in (0, 1, 2, 9, 10, 11, 18, 19, 20):
        cluster = 1
    elif cell in (3, 4, 5, 12, 13, 14, 21, 22, 23):
        cluster = 2
    elif cell in (6, 7, 8, 15, 16, 17, 24, 25, 26):
        cluster = 3
    elif cell in (27, 28, 29, 36, 13, 14, 21, 22, 23):
        cluster = 2

line = h_line_define(1)
print(line)
line = v_line_define(1)
print(line)


"""used to check if line and cluster generators work"""
# h_line_generator(8)
# print('h_line 2')
# print(h_line)
# v_line_generator(0)
# print('v_line 1')
# print(v_line)
# cluster_generator(0)
# print('cluster 1')
# print(cluster)

def cell_clear(cell):
    """used to check if the cell had a previous value inserted, will be default to true for 
    a sudoku starting from scratch"""
    if cell == 0:
        return True
    else:
        return False

# if cell_clear(cell):
#     cell = 1
#     if 






