# read animals.txt
file = open('animals.txt')
animals = file.readlines()
animals = map(lambda x: x.replace('\n', ''), animals)
file.close()
# and write animals_new.txt
new_file = open('animals_new.txt', mode='w')
new_file.write(' '.join(animals))
new_file.close()
