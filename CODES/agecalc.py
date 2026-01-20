'''An age calculator that takes your current age as input and calculates assuming maximum possible limit of your age as 90 years 
to give remaining dyas , months and weeks as output '''
age = input("What is Your Current age ? \n")
left = 90 - int(age)
months = int (left) * 12
weeks = int (left) * 52
days = int (left) * 365
print(f"You Have {months} months {weeks} weeks {days} days left.")