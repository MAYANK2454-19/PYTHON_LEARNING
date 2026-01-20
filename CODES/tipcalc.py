# A calculator that splits the bill with the percentage of tip we enter 
print("Welcome to the Tip Calculator\n")
bill = input("What was the total bill ? $")
tip = input("What is your percentage of tip ") 
person = input("Total number of people in which you have to split : \n")
final_bill = (((100 + float(tip))/100) * float(bill)) / int(person)
rounded_bill = round(final_bill , 2)
print(f"Each Person Should Pay : {rounded_bill}")