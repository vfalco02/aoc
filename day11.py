with open('./input_day11.txt') as f:
    inp = f.read()

inp = [list(x) for x in inp.split()]


def check_straight(layout, x, y):
    occupied = 0
    new_x = x
    for i in range(x, 0, -1):
        new_x = new_x - 1
        if new_x < 0:
            break
        if layout[new_x][y] == 'L':
            break
        if layout[new_x][y] == '#':
            occupied += 1
            break
    new_x = x
    for i in range(x, len(layout)):
        new_x = new_x + 1
        if new_x == len(layout):
            break
        if layout[new_x][y] == 'L':
            break
        if layout[new_x][y] == '#':
            occupied += 1
            break
    new_y = y
    for j in range(y, 0, -1):
        new_y = new_y - 1
        if new_y < 0:
            break
        if layout[x][new_y] == 'L':
            break
        if layout[x][new_y] == '#':
            occupied += 1
            break
    new_y = y
    for j in range(y, len(layout[0])):
        new_y = new_y + 1
        if new_y == len(layout[0]):
            break
        if layout[x][new_y] == 'L':
            break
        if layout[x][new_y] == '#':
            occupied += 1
            break
    return occupied

def check_diagonal(layout, x, y):
    occupied = 0
    found = False
    new_y = y
    new_x = x
    for i in range(x, 0, -1):
        new_x = new_x - 1
        new_y = new_y - 1
        if new_y < 0 or new_x < 0:
            break
        if layout[new_x][new_y] == 'L':
            break
        if layout[new_x][new_y] == '#':
            occupied += 1
            break
    new_y = y
    new_x = x
    for i in range(x, len(layout)):
        new_y = new_y - 1
        new_x = new_x + 1
        if new_y < 0 or new_x == len(layout):
            break
        if layout[new_x][new_y] == 'L':
            break
        if layout[new_x][new_y] == '#':
            occupied += 1
            break
    new_y = y
    new_x = x
    for i in range(x, 0, -1):
        new_y = new_y + 1
        new_x = new_x - 1
        if new_y == len(layout[x]) or new_x < 0:
            break
        if layout[new_x][new_y] == 'L':
            break
        if layout[new_x][new_y] == '#':
            occupied += 1
            break
    new_y = y
    new_x = x
    for i in range(x, len(layout)):
        new_y = new_y + 1
        new_x = new_x + 1
        if new_y == len(layout[x]) or new_x == len(layout):
            break
        if layout[new_x][new_y] == 'L':
            break
        if layout[new_x][new_y] == '#':
            occupied += 1
            break
    return occupied


def check_seat(layout, x, y):
    if layout[x][y] == '.':
        return -1
    occupied = 0
    occupied += check_diagonal(layout, x, y)
    occupied += check_straight(layout, x, y)
    return occupied

new_inp = []
while new_inp != inp:
    new_inp = [[y for y in x] for x in inp]
    for i in range(len(new_inp)):
        for j in range(len(new_inp[i])):
            num_occupied = check_seat(new_inp, i, j)
            if new_inp[i][j] == 'L' and num_occupied == 0:
                inp[i][j] = '#'
            elif new_inp[i][j] == '#' and num_occupied >= 5:
                inp[i][j] = 'L'

total_occupied = 0
for row in inp:
    total_occupied += row.count('#')
print(total_occupied)