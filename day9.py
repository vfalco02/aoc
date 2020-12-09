with open('./input_day9.txt') as f:
    inp = f.read()

inp = [int(x) for x in inp.split()]
found = False

for i in range(25, len(inp)):
    preamble = inp[i-25:i]
    found = False
    for first_num in preamble:
        for sec_num in preamble:
            if first_num == sec_num:
                continue
            if first_num + sec_num == inp[i]:
                found = True
                break
        if found == True:
            break
    else:
        print(f'Found it: {inp[i]}')
        found_value = inp[i]
        break


def whatever_to_call_this(full_inp, check_value):
    copied_list = [x for x in full_inp]
    equals = False
    while not equals:
        total = 0
        first_num = copied_list[0]
        for i in range(len(copied_list)):
            total += copied_list[i]
            if total > check_value:
                break
            if total == check_value:
                equals = True
                last_num = copied_list[i]
                break
        copied_list.pop(0)
    return first_num, last_num

first_num, last_num = whatever_to_call_this(inp, found_value)

final_list = inp[inp.index(first_num):inp.index(last_num)]
final_list.sort()
print(f'Sum of highest and lowest number in the range that sums up to {found_value}: {final_list[0]+final_list[-1]}')