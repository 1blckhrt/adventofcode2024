left = []
right = []
total = 0
total2 = 0

with open('input.txt', 'r') as file:
    for line in file:
        left_value, right_value = map(int, line.split())
        left.append(left_value)
        right.append(right_value)

sorted_left = sorted(left)
sorted_right = sorted(right)

for l, r in zip(sorted_left, sorted_right):
    total += abs(l - r)

print(total)

for l in sorted_left:
    total2 += l * sorted_right.count(l)
    
print(total2)