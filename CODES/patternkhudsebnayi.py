n=int(input())
for i in range (0,n):
    for j in range (0,n):
        if (j>0 and j < i and i != i-1):
            print(" ",end="")
        else:
            print("*",end="")
    print()        