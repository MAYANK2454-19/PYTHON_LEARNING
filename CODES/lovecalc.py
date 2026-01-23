print("Welcome to the The Love Calculator !")
name1 = input("What is your name ? \n").lower()
name2 = input("What is their name ? \n").lower()
t = int(name1.count("t")) + int(name2.count("t"))
r = int(name1.count("r")) + int(name2.count("r"))
u = int(name1.count("u")) + int(name2.count("u"))
e1 = int(name1.count("e")) + int(name2.count("e"))
l = int(name1.count("l")) + int(name2.count("l"))
o = int(name1.count("o")) + int(name2.count("o"))
v = int(name1.count("v")) + int(name2.count("v"))
e2 = int(name1.count("e")) + int(name2.count("e"))

love_score = str(t+r+u+e1) + str(l+o+v+e2)

if int(love_score) <=10 or int(love_score) >= 90 :
    print(f"Your love score is {love_score} , you go together like coke and mentos .")
elif 40 <= int(love_score) <= 50 :
    print(f"Your love score is {love_score} , you are alright together .")
else :
    print(f"Your score is {love_score}")