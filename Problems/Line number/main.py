# read sample.txt and print the number of lines
with open('sample.txt') as file:
    text = file.readlines()
    print(len(text))