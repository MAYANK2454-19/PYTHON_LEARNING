height = float (input("What is your height ? \n"))
weight = float (input("What is your weight ? \n"))
bmi_calc= (weight)/height ** 2
bmi = round(bmi_calc , 2)
print(f"Your BMI is {bmi}")
if bmi < 18.5 :
    print("You are Underweight !")
elif 18.5 <= bmi < 25 :
    print("You are Normal weight !")
elif 25 <= bmi < 30 :
    print("Your are Overweight !")
elif 30 <= bmi < 35 :
    print("Your are Obese !")
else :
    print("You are Clinically Obese")
