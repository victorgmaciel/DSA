
# import List, Set, Tuple

def grid_to_set(grid: list[list[int]]) -> set[tuple[int, int]]:
    my_set = set()

    for grid_column_index, grid_row in enumerate(grid):
        for index, value in enumerate(grid_row):
            if value == 1:
                temp_value = index, grid_column_index
                my_set.add(temp_value)

    return my_set








output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(output1)
# print(sorted(list(output1)))