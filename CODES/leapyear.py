year = int(input("Which year do yo want to check ? \n"))
if (year %  4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0) :
    print(f"Year {year} is a Leap year !")
else :
     print(f"Year {year} is a NOT a Leap year !")