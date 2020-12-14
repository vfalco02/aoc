with open('./input_day13.txt') as f:
    inp = f.read()

def find(ans, bus_value, bus_offset):
    while True:
        if (ans + bus_offset) % bus_value == 0:
            return ans
        ans += inc

buses = inp.split()[1].split(',')
buses = [(int(value), offset) for offset, value in enumerate(buses) if value.isnumeric()]
part2 = buses[0][0]
inc = 1

for bus in buses:
    part2 = find(part2, bus[0], bus[1])
    inc *= bus[0]

print(part2)