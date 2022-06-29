RED = (1, 0, 0, 0)
GREEN = (0, 1, 0, 0)
BLUE = (0, 0, 1, 0)
YELLOW = (0, 0, 0, 1)
CUBES = ["RYGRBG", "RBYBGY", "RBYGGB", "RRYBGR"]
COLORS = {
    "R": [1, 0, 0, 0],
    "G": [0, 1, 0, 0],
    "B": [0, 0, 1, 0],
    "Y": [0, 0, 0, 1]
}
COLOR_TO_LETTERS = {
    (1, 0, 0, 0): "R",
    (0, 1, 0, 0): "G",
    (0, 0, 1, 0): "B",
    (0, 0, 0, 1): "Y"
}
# Reducing values in ORIENTATION_LIST by 1 so that they match String indices instead of matching actual
# die sides.
ORIENTATION_LIST = [[1, 2, 4, 3], [2, 4, 3, 1], [4, 3, 1, 2], [3, 1, 2, 4], [5, 2, 0, 3], [2, 0, 3, 5],
                    [0, 3, 5, 2], [3, 5, 2, 0], [5, 2, 0, 3], [2, 0, 3, 5], [0, 3, 5, 2], [3, 5, 2, 0],
                    [4, 2, 1, 3], [2, 1, 3, 4], [1, 3, 4, 2], [3, 4, 2, 1], [1, 0, 4, 5], [0, 4, 5, 1],
                    [4, 5, 1, 0], [5, 1, 0, 4], [1, 5, 4, 0], [5, 4, 0, 1], [4, 0, 1, 5], [0, 1, 5, 4]]


def initialize_matrix():
    result = []
    for i in range(4):
        matrix_entry = []
        if i == 0:
            matrix_entry += [1, 0, 0, 0]
        if i == 1:
            matrix_entry += [0, 1, 0, 0]
        if i == 2:
            matrix_entry += [0, 0, 1, 0]
        if i == 3:
            matrix_entry += [0, 0, 0, 1]
        for j in range(24):
            for k in range(4):
                matrix_entry += (COLORS[CUBES[i][ORIENTATION_LIST[j][k]]])
            result.append(matrix_entry)
        print(result)


def show_colors(orientation, cube):
    result = ""
    for i in ORIENTATION_LIST[orientation]:
        result += CUBES[cube][i]
        print(i, result)
    return result


def generate_row(num, faces):
    row = [0, 0, 0, 0]
    row[num] = 1
    print(row)
    for i in faces:
        row += COLORS[i]
        print(row)
    return row


def display_row(vector):
    result = ""
    for x in range(4, len(vector), 4):
        result += COLOR_TO_LETTERS[tuple(vector[x:x + 4])]
    print(result)
    return result


def check_for_3(matrix):
    for i in range(4):  # determines column
        result = []
        for j in range(4):  # determines row
            result += display_row(matrix[j][i])
        print(result)


if __name__ == '__main__':
    matrix = [[[1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1] for i in range(10)] for j in range(10)]
    faces = show_colors(4, 2)
    row = generate_row(0, faces)
    display_row(row)
    check_for_3(matrix)
    initialize_matrix()