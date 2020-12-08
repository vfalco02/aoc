with open('./input_day8.txt') as f:
    inp = f.read()

inp = inp.split('\n')
inp = [line.split() for line in inp]

for j in range(len(inp)):
    i, accumulator = 0, 0
    new_inp = [[x[0], x[1]] for x in inp]
    if inp[j][0] == 'nop':
        new_inp[j][0] = 'jmp'
    elif inp[j][0] == 'jmp':
        new_inp[j][0] = 'nop'
    while new_inp[i] is not False:
        if new_inp[i][0] == 'acc':
            accumulator += int(new_inp[i][1])
        elif new_inp[i][0] == 'jmp':
            jmp = int(new_inp[i][1])
            new_inp[i] = False
            i += jmp
            continue
        new_inp[i] = False
        i += 1
        if i == len(new_inp):
            break
    if i == len(new_inp):
        break

print(accumulator)
