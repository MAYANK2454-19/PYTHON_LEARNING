age = int(input())
has_license = input() == "true"
has_insurance = input() == "true"

result = age>= 18 and has_license and has_insurance
print(result)