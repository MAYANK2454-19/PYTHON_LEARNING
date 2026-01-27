row1 = ["🟩","🟩","🟩"]
row2 = ["🟩","🟩","🟩"]
row3 = ["🟩","🟩","🟩"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
print(len(row1))
position = (input("where do you want to place the treasure ? \n"))
k = int(position)
a = int(k/10)
b=int(k-(a*10))
# print(a,b)
if (a == 1 and b == 1):
    row1[0]='x'
elif (a == 1 and b == 2):
    row2[0]='x'
elif (a == 1 and b == 3):
    row3[0]='x'
elif (a == 2 and b == 1):
    row1[1]='x'
elif (a == 2 and b == 2):
    row2[1]='x'
elif (a == 2 and b == 3):
    row3[1]='x'
elif (a == 3 and b == 1):
    row1[2]='x'
elif (a == 3 and b == 2):
    row2[2]='x'
elif (a == 3 and b == 3):
    row3[2]='x'
else :
    print("Invalid input")
print(f"{row1}\n{row2}\n{row3}")