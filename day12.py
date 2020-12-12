# inp = '''F10
# N3
# F7
# R90
# F11'''

with open('./input_day12.txt') as f:
    inp = f.read()

inp = inp.split()
inp = [(x[0], int(x[1:])) for x in inp]

ship_x = ship_y = 0
wp_x = 10
wp_y = 1
cur_deg = 90

def move_wp(direction, amt):
    x = y = 0
    if direction == 'E':
        x += amt
    elif direction == 'W':
        x -= amt
    elif direction == 'N':
        y += amt
    elif direction == 'S':
        y -= amt
    return x, y

def move_ship(wp_x, wp_y, amt):
    x = wp_x * amt
    y = wp_y * amt
    return x, y

def rotate(wp_x, wp_y, direction, degrees):
    if direction == 'L':
        if degrees == 90:
            degrees = 270
        elif degrees == 270:
            degrees = 90
    if degrees == 90:
        new_x = wp_y
        new_y = -wp_x
    elif degrees == 180:
        new_x = -wp_x
        new_y = -wp_y
    elif degrees == 270:
        new_x = -wp_y
        new_y = wp_x
    return new_x, new_y

for i in range(len(inp)):
    if inp[i][0] == 'F':
        new_x, new_y = move_ship(wp_x, wp_y, inp[i][1])
        ship_x += new_x
        ship_y += new_y
    elif inp[i][0] in ['N', 'S', 'E', 'W']:
        new_x, new_y = move_wp(inp[i][0], inp[i][1])
        wp_x += new_x
        wp_y += new_y
    elif inp[i][0] in ['L', 'R']:
        wp_x, wp_y = rotate(wp_x, wp_y, inp[i][0], inp[i][1])

print(ship_x,ship_y)
print (abs(ship_x) + abs(ship_y))
