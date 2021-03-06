# read sums.txt
with open('sums.txt') as file:
    for line in file.readlines():
        print(sum([int(x) for x in line.split(' ')]))