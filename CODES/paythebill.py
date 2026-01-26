import random 
names_string = input("Give me names of everyone , separated with a comma ")
names=names_string.split(", ")
num = int (len(names))
a = random.randint(0,(num-1))
print(f"{names[a]} is going to pay the bill.")