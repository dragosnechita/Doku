from functions import print_table, generate_index_table
from math import floor
sudoku = []


"""used to see the whole sudoku layout"""
# generate_index_table(sudoku)
# print_table(sudoku)


def h_line_generator(h_line):
    h_line_list = []
    """used to generate a horizontal line to check whether the current cell value respects 
    the principles of Sudoku"""
    for cell in range(h_line * 9, h_line * 9 + 9):
        index_out_of_range(h_line_list, sudoku, cell)
        # try:
        #     h_line_list.append(sudoku[cell])
        # except IndexError:
        #     h_line_list.append(0)
    return h_line_list


def v_line_generator(v_line):
    """used to generate a vertical line to check whether the current cell value respects 
    the principles of Sudoku"""
    v_line_list = []
    for cell in range(v_line, 80, 9):
        try:
            v_line_list.append(sudoku[cell])
        except IndexError:
            v_line_list.append(0)
    return v_line_list

def append_cluster_values(cluster):
    """used for generating cluster values in cluster generator, based on cluster number"""
    cluster_gen = []
    for cell in range(cluster, cluster + 3):
        try:
            cluster_gen.append(sudoku[cell])
        except IndexError:
            cluster_gen.append(0)
    for cell in range(cluster + 9, cluster + 12):
        try:
            cluster_gen.append(sudoku[cell])
        except IndexError:
            cluster_gen.append(0)
    for cell in range(cluster + 18 , cluster + 21):
        try:
            cluster_gen.append(sudoku[cell])
        except IndexError:
            cluster_gen.append(0)
    return cluster_gen

def cluster_generator(cluster):
    cluster_list = []
    """used to generate a cluster of 3by3 cells to check whether the current cell value respects 
    the principles of Sudoku"""
    """needs to be made more efficient (with less code)"""
    if cluster < 3:
        cluster *= 3
        cluster_list = append_cluster_values(cluster)
    elif cluster == 3:
        cluster *= 9
        cluster_list = append_cluster_values(cluster)
    elif cluster == 4:
        cluster *= 7
        cluster +=2
        cluster_list = append_cluster_values(cluster)
    elif cluster == 5:
        cluster *= 6
        cluster += 3
        cluster_list = append_cluster_values(cluster)
    elif cluster == 6:
        cluster *= 9
        cluster_list = append_cluster_values(cluster)
    elif cluster == 7:
        cluster *= 8
        cluster += 1
        cluster_list = append_cluster_values(cluster)
    elif cluster == 8:
        cluster *= 7
        cluster += 4
        cluster_list = append_cluster_values(cluster)
    return cluster_list

def h_line_define(cell):
    """used to find out which h line should be generated to check sudoku rules"""
    h_line = floor(cell / 9)
    return h_line

def v_line_define(cell):
    """used to find out which v line should be generated to check sudoku rules"""
    v_line = cell % 9
    return v_line

def cluster_define(cell):
    """used to identify the cluster to which the cellbelongs to"""
    for cluster_number in range (0,9):
        if cell in cluster_generator(cluster_number):
            cluster = cluster_number
            return cluster
        else:
            continue

def index_out_of_range(stack,right_cell, right_index, wrong_cell=0):
    try:
        stack.append(right_cell[right_index])
    except IndexError:
        stack.append(wrong_cell)

def cell_clear(cell):
    """used to check if the cell had a previous value inserted, will be default to true for 
    a sudoku starting from scratch"""
    if cell == 0:
        return True
    else:
        return False

print(h_line_generator(0))
print(v_line_generator(0))
print(cluster_generator(0))


"""script used for testing cluster generators"""
# for cluster in range (9):
#     print(f"cluster number {cluster}")
#     print(cluster_generator(cluster))
# print(cluster_generator(0))
# print('cluster_define check')
# print(cluster_define(18))

# line = h_line_define(1)
# print(line)
# line = v_line_define(1)
# print(line)


"""used to check if line and cluster generators work"""
# h_line_generator(8)
# print('h_line_list')
# print(h_line_list)
# v_line_generator(0)
# print('v_line_list')
# print(v_line_list)
# cluster_generator(0)
# print('cluster_list')
# print(cluster_list)



# if cell_clear(cell):
#     cell = 1
#     if 






