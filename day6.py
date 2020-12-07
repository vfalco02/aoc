from string import ascii_lowercase

with open('./input.txt') as f:
    groups = f.read()

group_sizes = [len(x.split('\n')) for x in groups.split('\n\n')]
groups = [x.replace('\n', '') for x in groups.split('\n\n')]

total = 0
for group in range(len(groups)):
    for letter in ascii_lowercase:
        if group_sizes[group] == groups[group].count(letter):
            total += 1

print(total)
