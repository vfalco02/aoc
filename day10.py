with open('./input_day10.txt') as f:
    inp = f.read()

inp = [int(i) for i in inp.splitlines()]
inp.sort()

outlet, device = 0, max(inp) + 3
joltages = [outlet] + inp + [device]

diffs = [a - b for a, b in zip(joltages[1:], joltages)]

print(f"Day 10 Part 1: {diffs.count(1) * diffs.count(3)}")

results = [0 for _ in range(device + 1)]
results[0] = 1
for joltage in joltages:
    results[joltage] += results[joltage - 1] + results[joltage - 2] + results[joltage - 3]

print(f"Day 10 Part 2: {results[-1]}")