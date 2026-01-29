import random 
names_string = input("Give me names of everyone , separated with a comma ")
names=names_string.split(",")
# num = int (len(names))
# a = random.randint(0,(num-1))
# using the choice function
a=random.choice(names)
print(f"{a} is going to pay the bill.")