"""main file for the Sudoku Exercise"""


class Cell():
    """The class of the cell used"""
    def __init__(self, value=0):
        self.value = value


def temp_update_cell(group):
    """Temporary function for incremental update of one group (used for esting)"""
    temp_num = 1
    for our_cell in group:
        update_cell_value(our_cell, temp_num)
        temp_num += 1


def update_cell_value(cell, value):
    """simple cell value update"""
    cell.value = value


def check_unique(cell_value, group):
    """Function to check unique value of a cell in it's group"""
    temp_check_list = []
    for item in group:
        temp_check_list.append(item.value)
    if temp_check_list.count(cell_value) == 1:
        return True

    return False


def print_table():
    """A function to print data in sudoku table form"""
    print("-" * 25)
    print(f"| {c_1_1.value} {c_1_2.value} {c_1_3.value} "
          f"| {c_1_4.value} {c_1_5.value} {c_1_6.value} "
          f"| {c_1_7.value} {c_1_8.value} {c_1_9.value} | \n"
          f"| {c_2_1.value} {c_2_2.value} {c_2_3.value} "
          f"| {c_2_4.value} {c_2_5.value} {c_2_6.value} "
          f"| {c_2_7.value} {c_2_8.value} {c_2_9.value} | \n"
          f"| {c_3_1.value} {c_3_2.value} {c_3_3.value} "
          f"| {c_3_4.value} {c_3_5.value} {c_3_6.value} "
          f"| {c_3_7.value} {c_3_8.value} {c_3_9.value} |")
    print("-" * 25)
    print(f"| {c_4_1.value} {c_4_2.value} {c_4_3.value} "
          f"| {c_4_4.value} {c_4_5.value} {c_4_6.value} "
          f"| {c_4_7.value} {c_4_8.value} {c_4_9.value} | \n"
          f"| {c_5_1.value} {c_5_2.value} {c_5_3.value} "
          f"| {c_5_4.value} {c_5_5.value} {c_5_6.value} "
          f"| {c_5_7.value} {c_5_8.value} {c_5_9.value} | \n"
          f"| {c_6_1.value} {c_6_2.value} {c_6_3.value} "
          f"| {c_6_4.value} {c_6_5.value} {c_6_6.value} "
          f"| {c_6_7.value} {c_6_8.value} {c_6_9.value} |")
    print("-" * 25)
    print(f"| {c_7_1.value} {c_7_2.value} {c_7_3.value} "
          f"| {c_7_4.value} {c_7_5.value} {c_7_6.value} "
          f"| {c_7_7.value} {c_7_8.value} {c_7_9.value} | \n"
          f"| {c_8_1.value} {c_8_2.value} {c_8_3.value} "
          f"| {c_8_4.value} {c_8_5.value} {c_8_6.value} "
          f"| {c_8_7.value} {c_8_8.value} {c_8_9.value} | \n"
          f"| {c_9_1.value} {c_9_2.value} {c_9_3.value} "
          f"| {c_9_4.value} {c_9_5.value} {c_9_6.value} "
          f"| {c_9_7.value} {c_9_8.value} {c_9_9.value} |")
    print("-" * 25)


# Cell creation
c_1_1, c_1_2, c_1_3, c_1_4, c_1_5, c_1_6, c_1_7, c_1_8, c_1_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
c_2_1, c_2_2, c_2_3, c_2_4, c_2_5, c_2_6, c_2_7, c_2_8, c_2_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
c_3_1, c_3_2, c_3_3, c_3_4, c_3_5, c_3_6, c_3_7, c_3_8, c_3_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
c_4_1, c_4_2, c_4_3, c_4_4, c_4_5, c_4_6, c_4_7, c_4_8, c_4_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
c_5_1, c_5_2, c_5_3, c_5_4, c_5_5, c_5_6, c_5_7, c_5_8, c_5_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
c_6_1, c_6_2, c_6_3, c_6_4, c_6_5, c_6_6, c_6_7, c_6_8, c_6_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
c_7_1, c_7_2, c_7_3, c_7_4, c_7_5, c_7_6, c_7_7, c_7_8, c_7_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
c_8_1, c_8_2, c_8_3, c_8_4, c_8_5, c_8_6, c_8_7, c_8_8, c_8_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
c_9_1, c_9_2, c_9_3, c_9_4, c_9_5, c_9_6, c_9_7, c_9_8, c_9_9 = \
    Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0)
# Cluster creation
cluster_1 = [c_1_1, c_1_2, c_1_3, c_2_1, c_2_2, c_2_3, c_3_1, c_3_2, c_3_3]
cluster_2 = [c_1_4, c_1_5, c_1_6, c_2_4, c_2_5, c_2_6, c_3_4, c_3_5, c_3_6]
cluster_3 = [c_1_7, c_1_8, c_1_9, c_2_7, c_2_8, c_2_9, c_3_7, c_3_8, c_3_9]
cluster_4 = [c_4_1, c_4_2, c_4_3, c_5_1, c_5_2, c_5_3, c_6_1, c_6_2, c_6_3]
cluster_5 = [c_4_4, c_4_5, c_4_6, c_5_4, c_5_5, c_5_6, c_6_4, c_6_5, c_6_6]
cluster_6 = [c_4_7, c_4_8, c_4_9, c_5_7, c_5_8, c_5_9, c_6_7, c_6_8, c_6_9]
cluster_7 = [c_7_1, c_7_2, c_7_3, c_8_1, c_8_2, c_8_3, c_9_1, c_9_2, c_9_3]
cluster_8 = [c_7_4, c_7_5, c_7_6, c_8_4, c_8_5, c_8_6, c_9_4, c_9_5, c_9_6]
cluster_9 = [c_7_7, c_7_8, c_7_9, c_8_7, c_8_8, c_8_9, c_9_7, c_9_8, c_9_9]
# Every horizontal
h_line_1 = [c_1_1, c_1_2, c_1_3, c_1_4, c_1_5, c_1_6, c_1_7, c_1_8, c_1_9]
h_line_2 = [c_2_1, c_2_2, c_2_3, c_2_4, c_2_5, c_2_6, c_2_7, c_2_8, c_2_9]
h_line_3 = [c_3_1, c_3_2, c_3_3, c_3_4, c_3_5, c_3_6, c_3_7, c_3_8, c_3_9]
h_line_4 = [c_4_1, c_4_2, c_4_3, c_4_4, c_4_5, c_4_6, c_4_7, c_4_8, c_4_9]
h_line_5 = [c_5_1, c_5_2, c_5_3, c_5_4, c_5_5, c_5_6, c_5_7, c_5_8, c_5_9]
h_line_6 = [c_6_1, c_6_2, c_6_3, c_6_4, c_6_5, c_6_6, c_6_7, c_6_8, c_6_9]
h_line_7 = [c_7_1, c_7_2, c_7_3, c_7_4, c_7_5, c_7_6, c_7_7, c_7_8, c_7_9]
h_line_8 = [c_8_1, c_8_2, c_8_3, c_8_4, c_8_5, c_8_6, c_8_7, c_8_8, c_8_9]
h_line_9 = [c_9_1, c_9_2, c_9_3, c_9_4, c_9_5, c_9_6, c_9_7, c_9_8, c_9_9]
# Every vertical line
v_line_1 = [c_1_1, c_2_1, c_3_1, c_4_1, c_5_1, c_6_1, c_7_1, c_8_1, c_9_1]
v_line_2 = [c_1_2, c_2_2, c_3_2, c_4_2, c_5_2, c_6_2, c_7_2, c_8_2, c_9_2]
v_line_3 = [c_1_3, c_2_3, c_3_3, c_4_3, c_5_3, c_6_3, c_7_3, c_8_3, c_9_3]
v_line_4 = [c_1_4, c_2_4, c_3_4, c_4_4, c_5_4, c_6_4, c_7_4, c_8_4, c_9_4]
v_line_5 = [c_1_5, c_2_5, c_3_5, c_4_5, c_5_5, c_6_5, c_7_5, c_8_5, c_9_5]
v_line_6 = [c_1_6, c_2_6, c_3_6, c_4_6, c_5_6, c_6_6, c_7_6, c_8_6, c_9_6]
v_line_7 = [c_1_7, c_2_7, c_3_7, c_4_7, c_5_7, c_6_7, c_7_7, c_8_7, c_9_7]
v_line_8 = [c_1_8, c_2_8, c_3_8, c_4_8, c_5_8, c_6_8, c_7_8, c_8_8, c_9_8]
v_line_9 = [c_1_9, c_2_9, c_3_9, c_4_9, c_5_9, c_6_9, c_7_9, c_8_9, c_9_9]

if __name__ == "__main__":
    temp_update_cell(v_line_1)
    print_table()
    print(check_unique(c_1_1.value, v_line_1))
