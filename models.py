class Cell():
    """The class of the cell used"""
    def __init__(self, value=0, change=True):
        self.value = value
        self.change = True


def temp_update_cell(group):
    """Temporary function for incremental update of one group (used for esting)"""
    temp_num = 1
    for our_cell in group:
        update_cell_value(our_cell, temp_num)
        temp_num += 1


def update_cell_value(cell, value):
    """simple cell value update"""
    cell.value = value


def check_unique(cell, group):
    """Function to check unique value of a cell in it's group"""
    temp_check_list = []
    for item in group:
        temp_check_list.append(item.value)
    if temp_check_list.count(cell.value) == 1:
        return True
    return False


def current_cluster(cell):
    current_cluster = 0  # used for checking the unique cell value in current cluster
    for cluster in all_clusters:
        if cell in cluster:
            current_cluster = cluster
    return current_cluster


def current_h_line(cell):
    for h_line in all_h_lines:
        if cell in h_line:
            current_h_line = h_line
    return current_h_line

def current_v_line(cell):
    for v_line in all_v_lines:
        if cell in v_line:
            current_v_line = v_line
    return current_v_line

def solve(cell):
    """Function to fill one cell at a time"""
    if not cell.change:
        cell.value = cell.value
        return cell.value
    else:
        cell.value = 1
        while cell.value <= 9:
            if check_unique(cell, current_cluster(cell)) and check_unique(cell, current_h_line(cell)) and check_unique(cell, current_v_line(cell)):
                return cell.value
                break
            else:
                cell.value += 1
        cell.value = "X"

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

# Cluster creation


if __name__ == "__main__":
cluster_1 = [c_1_1, c_1_2, c_1_3, c_2_1, c_2_2, c_2_3, c_3_1, c_3_2, c_3_3]
cluster_2 = [c_1_4, c_1_5, c_1_6, c_2_4, c_2_5, c_2_6, c_3_4, c_3_5, c_3_6]
cluster_3 = [c_1_7, c_1_8, c_1_9, c_2_7, c_2_8, c_2_9, c_3_7, c_3_8, c_3_9]
cluster_4 = [c_4_1, c_4_2, c_4_3, c_5_1, c_5_2, c_5_3, c_6_1, c_6_2, c_6_3]
cluster_5 = [c_4_4, c_4_5, c_4_6, c_5_4, c_5_5, c_5_6, c_6_4, c_6_5, c_6_6]
cluster_6 = [c_4_7, c_4_8, c_4_9, c_5_7, c_5_8, c_5_9, c_6_7, c_6_8, c_6_9]
cluster_7 = [c_7_1, c_7_2, c_7_3, c_8_1, c_8_2, c_8_3, c_9_1, c_9_2, c_9_3]
cluster_8 = [c_7_4, c_7_5, c_7_6, c_8_4, c_8_5, c_8_6, c_9_4, c_9_5, c_9_6]
cluster_9 = [c_7_7, c_7_8, c_7_9, c_8_7, c_8_8, c_8_9, c_9_7, c_9_8, c_9_9]
all_clusters = [cluster_1, cluster_2, cluster_3, cluster_4, cluster_5,
                cluster_6, cluster_7, cluster_8, cluster_9]
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
all_h_lines = [h_line_1, h_line_2, h_line_3, h_line_4, h_line_5, h_line_6,
               h_line_7, h_line_8, h_line_9]
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
all_v_lines = [v_line_1, v_line_2, v_line_3, v_line_4, v_line_5, v_line_6,
               v_line_7, v_line_8, v_line_9]
  
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

    print_table()
    # print(c_1_1.value, c_1_1.change)
    # print(solve(c_1_1))
    # print(solve(c_1_2))
    # print(solve(c_1_3))
    # solve(c_2_1)
    # solve(c_2_2)
    # solve(c_2_3)
    # solve(c_3_1)
    # solve(c_3_2)
    # solve(c_3_3)
    for cell in cluster_1:
        solve(cell)
    for cell in cluster_2:
        solve(cell)
    for cell in cluster_3:
        solve(cell)
    print_table()