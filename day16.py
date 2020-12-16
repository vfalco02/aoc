with open('./input_day16.txt') as f:
    inp = f.read()

rules, my_ticket, nearby_tickets = inp.split('\n\n')
rules = rules.split('\n')
my_ticket = [int(x) for x in my_ticket.split('\n')[1].split(',')]
nearby_tickets = nearby_tickets.split('nearby tickets:\n')[1].split()
nearby_tickets = [ticket.split(',') for ticket in nearby_tickets]
valid_nums = []

rule_dict = {}
# Get range for all rules
for rule in range(len(rules)):
    values_list = rules[rule].split(': ')
    rule_dict[values_list[0]] = []
    values = values_list[1].split(' or ')
    rules[rule] = []
    for value in values:
        low = int(value.split('-')[0])
        high = int(value.split('-')[1])
        for i in range(low, high+1):
            valid_nums.append(i)
            rule_dict[values_list[0]].append(i)

# Fitler out invalid tickets
good_tickets = [ticket for ticket in nearby_tickets]
for ticket in range(len(nearby_tickets)):
    for value in nearby_tickets[ticket]:
        if int(value) not in valid_nums:
            good_tickets.remove(nearby_tickets[ticket])
            break

# Find rule possibilites for each ticket
possibilities = {key: [] for key in rule_dict}
for key in rule_dict:
    for i in range(len(good_tickets[0])):
        cache = []
        for ticket in good_tickets:
            if int(ticket[i]) in rule_dict[key]:
                cache.append(True)
            else:
                cache.append(False)
        if all(cache):
            possibilities[key].append(i)

# Get the unique index for each rule
cache = {}
new_dict = {key: possibilities[key] for key in possibilities}
while True:
    possibilities = {key: new_dict[key] for key in new_dict}
    if not possibilities:
        break
    for key in possibilities:
        if len(possibilities[key]) == 1:
            cache[key] = possibilities[key][0]
            new_dict.pop(key)
            for key2 in new_dict:
                if cache.get(key) in new_dict[key2]:
                    new_dict[key2].remove(cache[key])

total = 1
for key in cache:
    if 'departure' in key:
        total *= my_ticket[cache[key]]
