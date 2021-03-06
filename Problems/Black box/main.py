# use the function blackbox(lst) that is already defined
lst = [4,5,6]
print("modifies" if id(lst) == id(blackbox(lst)) else "new")