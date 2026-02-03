import random
password =""
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
print("Welcome! to MyPass generator")
print(len(letters))
print(len(numbers))
print(len(symbols))
n=(random.randint(0,len(numbers)))
l=(random.randint(0,len(letters)))
s=(random.randint(0,len(symbols)))
nr_letters=int(input("How many letters you want in your password \n"))
nr_numbers=int(input("How many digits you want in your password \n"))
nr_symbols=int(input("How many symbols you want in your password \n"))
for num in range (0,nr_numbers+1) :
    password +=numbers[n] 
for num in range (0,nr_letters+1) :
    password +=numbers[l] 
for num in range (0,nr_symbols+1) :
    password +=numbers[s] 
print(password)