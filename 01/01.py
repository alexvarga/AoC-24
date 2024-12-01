leftList = []
rightList= []

with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]


for item in input_lines:
    new = item.split(' ')
    leftList.append(int(new[0]))
    rightList.append(int(new[-1]))


_ = leftList.sort()
_ = rightList.sort()


differences = [x - y for x, y in zip(leftList, rightList)]

total = 0
for item in differences:
    total=total+abs(item)

print(total)


counts=[]

for number in leftList:
    counts.append(rightList.count(number)*number)

print(sum(counts))