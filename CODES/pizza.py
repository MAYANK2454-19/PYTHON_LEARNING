#A pizza order calculator that calculates the final bill on  the basis of selcetions by the customer

print("Welcome ! to Python Pizza Deliveries\n")
print("Small = $15")
print("Medium = $20")
print("Large = $25")
print("Pepperoni for small = $2")
print("Pepperoni for medium and large = $3")
print("Extra cheese = $1")

size = input("Which size Pizza do you want ? S , M , L \n")
add_pepperoni = input("Do you want extra Pepproni ? Y or N \n")
extra_cheese = input("Do you want extra cheese ? Y or N \n")
bill = 0 

if size == "s" or size == " S " :
    bill += 15 
    if add_pepperoni == "y" or add_pepperoni ==  "Y" :
        bill += 2 
    if extra_cheese == "y" or extra_cheese == "Y" :
        bill += 1

elif size == "m" or size == " M " :
    bill += 20
    if add_pepperoni == "y" or add_pepperoni == "Y" :
        bill += 3 
    if extra_cheese == "y" or extra_cheese == "Y" :
        bill += 1 

elif size == "l" or size == " L " :
    bill += 25 
    if add_pepperoni == "y" or add_pepperoni == "Y" :
        bill += 3 
    if extra_cheese == "y" or extra_cheese == "Y" :
        bill += 1 

else :
    print("Slect a Valid Choice !!!")   

print(f"Size = {size}")
print(f"Pepperoni = {add_pepperoni}")
print(f"Extra Cheese = {extra_cheese}\n")
print(f"Your final bill is ${bill}\n")
