nums = [12, 1, 16, 3, 11, 0]
tracker = {nums[i]: (i, 0, True) for i in range(len(nums))}

for i in range(len(nums), 30000000):
    if tracker[nums[i-1]][2] == True:
        nums.append(0)
        tracker[0] = (i, tracker[0][0], False)
    elif tracker[nums[i-1]][2] == False:
        next_num = tracker[nums[i-1]][0] - tracker[nums[i-1]][1]
        nums.append(next_num)
        if next_num in tracker:
            tracker[next_num] = (i, tracker[next_num][0], False)
        else:
            tracker[next_num] = (i, i, True)

print(nums[-1])