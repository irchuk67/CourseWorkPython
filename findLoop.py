import random

FIELD_SIZE = 10
class Cell:
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column and self.color == other.color

    def __ne__(self, other):
        return not self.__eq__(other)


class Node:
    def __init__(self, current, parent=None, children=None):
        self.cell = current
        self.parent = parent
        self.children = children if children is not None else []

    def set_children(self, children):
        self.children = children

    def get_cell(self):
        return self.cell

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children


W = "0"
B = "X"
E = "-"
VISITED = "#"


def print_field(field):
    for row in field:
        print(" ".join(row))
    print()


def find_first_cells(field, node):
    cells = []
    current_cell = node.get_cell()
    if current_cell.row + 1 < FIELD_SIZE:
        cells.append(Cell(current_cell.row + 1, current_cell.column, field[current_cell.row + 1][current_cell.column]))
    if current_cell.row - 1 >= 0:
        cells.append(Cell(current_cell.row - 1, current_cell.column, field[current_cell.row - 1][current_cell.column]))
    if current_cell.column + 1 < FIELD_SIZE:
        cells.append(Cell(current_cell.row, current_cell.column + 1, field[current_cell.row][current_cell.column + 1]))
    if current_cell.column - 1 >= 0:
        cells.append(Cell(current_cell.row, current_cell.column - 1, field[current_cell.row][current_cell.column - 1]))
    return cells


def find_next_cells(field, node):
    cells = []
    parent = node.get_parent()
    parent_cell = parent.get_cell()
    current_cell = node.get_cell()
    if parent_cell.color == W:
        if abs(current_cell.row - parent_cell.row) == 1:
            if current_cell.column - 1 >= 0:
                cells.append(
                    Cell(current_cell.row, current_cell.column - 1, field[current_cell.row][current_cell.column - 1]))
            if current_cell.column + 1 < FIELD_SIZE:
                cells.append(
                    Cell(current_cell.row, current_cell.column + 1, field[current_cell.row][current_cell.column + 1]))
        else:
            if current_cell.row - 1 >= 0:
                cells.append(
                    Cell(current_cell.row - 1, current_cell.column, field[current_cell.row - 1][current_cell.column]))
            if current_cell.row + 1 < FIELD_SIZE:
                cells.append(
                    Cell(current_cell.row + 1, current_cell.column, field[current_cell.row + 1][current_cell.column]))
        return cells

    if parent_cell.color == B:
        if current_cell.row - parent_cell.row == 1 and current_cell.row + 1 < FIELD_SIZE:
            cells.append(
                Cell(current_cell.row + 1, current_cell.column, field[current_cell.row + 1][current_cell.column]))
        if current_cell.row - parent_cell.row == -1 and current_cell.row - 1 >= 0:
            cells.append(
                Cell(current_cell.row - 1, current_cell.column, field[current_cell.row - 1][current_cell.column]))
        if current_cell.column - parent_cell.column == 1 and current_cell.column + 1 < FIELD_SIZE:
            cells.append(
                Cell(current_cell.row, current_cell.column + 1, field[current_cell.row][current_cell.column + 1]))
        if current_cell.column - parent_cell.column == -1 and current_cell.column - 1 >= 0:
            cells.append(
                Cell(current_cell.row, current_cell.column - 1, field[current_cell.row][current_cell.column - 1]))
        return cells

    if field[current_cell.row][current_cell.column] == W:
        if current_cell.row - parent_cell.row == 1:
            if current_cell.row + 1 < FIELD_SIZE:
                if field[current_cell.row + 1][current_cell.column] != W:
                    cells.append(Cell(current_cell.row + 1, current_cell.column,
                                      field[current_cell.row + 1][current_cell.column]))
        if current_cell.row - parent_cell.row == -1:
            if current_cell.row - 1 >= 0:
                if field[current_cell.row - 1][current_cell.column] != W:
                    cells.append(Cell(current_cell.row - 1, current_cell.column,
                                      field[current_cell.row - 1][current_cell.column]))
        if current_cell.column - parent_cell.column == 1:
            if current_cell.column + 1 < FIELD_SIZE:
                if field[current_cell.row][current_cell.column + 1] != W:
                    cells.append(Cell(current_cell.row, current_cell.column + 1,
                                      field[current_cell.row][current_cell.column + 1]))
        if current_cell.column - parent_cell.column == -1:
            if current_cell.column - 1 >= 0:
                if field[current_cell.row][current_cell.column - 1] != W:
                    cells.append(Cell(current_cell.row, current_cell.column - 1,
                                      field[current_cell.row][current_cell.column - 1]))
    elif field[current_cell.row][current_cell.column] == B:
        if abs(current_cell.row - parent_cell.row) == 1:
            if FIELD_SIZE > current_cell.column + 2:
                if field[current_cell.row][current_cell.column + 1] != B:
                    cells.append(Cell(current_cell.row, current_cell.column + 1,
                                      field[current_cell.row][current_cell.column + 1]))
            if current_cell.column - 2 >= 0:
                if field[current_cell.row][current_cell.column - 1] != B:
                    cells.append(Cell(current_cell.row, current_cell.column - 1,
                                      field[current_cell.row][current_cell.column - 1]))
        else:
            if current_cell.row - 2 >= 0:
                if field[current_cell.row - 1][current_cell.column] != B:
                    cells.append(Cell(current_cell.row - 1, current_cell.column,
                                      field[current_cell.row - 1][current_cell.column]))
            if FIELD_SIZE > current_cell.row + 2:
                if field[current_cell.row + 1][current_cell.column] != B:
                    cells.append(Cell(current_cell.row + 1, current_cell.column,
                                      field[current_cell.row + 1][current_cell.column]))
    else:
        if current_cell.row - parent_cell.row == 1 and current_cell.row + 1 < FIELD_SIZE:
            cells.append(
                Cell(current_cell.row + 1, current_cell.column, field[current_cell.row + 1][current_cell.column]))
        if current_cell.row - parent_cell.row == -1 and current_cell.row - 1 >= 0:
            cells.append(
                Cell(current_cell.row - 1, current_cell.column, field[current_cell.row - 1][current_cell.column]))
        if current_cell.column - parent_cell.column == 1 and current_cell.column + 1 < FIELD_SIZE:
            cells.append(
                Cell(current_cell.row, current_cell.column + 1, field[current_cell.row][current_cell.column + 1]))
        if current_cell.column - parent_cell.column == -1 and current_cell.column - 1 >= 0:
            cells.append(
                Cell(current_cell.row, current_cell.column - 1, field[current_cell.row][current_cell.column - 1]))
    return cells


def check_cell_already_in_branch(node, cell):
    if node.get_cell() == cell and node.get_parent() is not None:
        return True
    if node.get_parent() is None:
        return False
    return check_cell_already_in_branch(node.get_parent(), cell)


def build_graph(node, field, get_cells):
    cells = get_cells(field, node)
    children = []
    for cell in cells:
        if check_cell_already_in_branch(node, cell):
            continue
        child = build_graph(Node(cell, node), field, find_next_cells)
        children.append(child)
    node.set_children(children)
    return node


def print_circular_loop(loop, field):
    for node in loop:
        field[node.get_cell().row][node.get_cell().column] = VISITED
    print("Field with circular loop:")
    print_field(field)


def traverse_graph(node, path, start_cell, field, found, modify):
    if node.get_cell() == start_cell and node.get_parent() is not None:
        if modify:
            print_circular_loop(path, field)
        return True
    if not node.get_children():
        return False
    for child in node.get_children():
        loop = path + [child]
        return traverse_graph(child, loop, start_cell, field, found, modify)
    return found


def find_circular_loop(field, modify):
    found = False
    counter = 0
    while counter <= 1000:
        start_i = random.randint(0, FIELD_SIZE - 1)
        start_j = random.randint(0, FIELD_SIZE - 1)
        start_cell = Cell(start_i, start_j, field[start_i][start_j])
        start_node = build_graph(Node(start_cell), field, find_first_cells)
        path = [start_node]
        found = traverse_graph(start_node, path, start_cell, field, found, modify)
        counter += 1
        if found:
            return True
    return False


cells = [
    [B, E, E, E, E, B, E, E, E, E],
    [E, E, E, W, E, W, E, B, E, E],
    [E, B, E, W, E, E, E, B, E, E],
    [E, W, E, E, E, W, E, E, B, E],
    [E, E, W, B, E, B, E, E, W, E],
    [E, B, E, E, W, E, W, B, E, E],
    [E, W, E, E, B, E, E, E, B, E],
    [E, E, W, E, E, E, B, E, W, E],
    [E, E, B, E, B, E, W, E, E, E],
    [E, E, E, E, W, E, E, E, E, B]
]

result = find_circular_loop(cells, True)
