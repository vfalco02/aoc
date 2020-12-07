import re

with open('./input_day7.txt') as f:
    rules = f.read()

rules = [x.split(' bags contain ') for x in rules.split('\n')]
rules = {x[0]: x[1].replace(' bags', '').replace(' bag', '') for x in rules}
rule_dict = {}
for rule in rules:
    rule_dict[rule] = {}
    m = re.findall('(\d)(\D*)', rules[rule])
    for result in m:
        rule_dict[rule].update({
            result[1].replace(',', '').replace('.', '').strip(): result[0]
        })

first_bag = ['shiny gold']

def count_bags(bags_to_count, current_total):
    total = 0
    next_bags = []
    for bag in bags_to_count:
        for bag_type in rule_dict[bag]:
            total += int(rule_dict[bag][bag_type])
            for num_of_bags in range(int(rule_dict[bag][bag_type])):
                next_bags.append(bag_type)
    if not next_bags:
        return current_total + total
    return count_bags(next_bags, current_total + total)

print(count_bags(first_bag, 0))