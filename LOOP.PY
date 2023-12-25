for i in range (1,6) :
    for j in range (i) :
        if i%2 ==0 : print("#",end="")
        else : print("*",end="")
    print("")

print("")

for i in range (1,6) :
    for j in range (6-i) :
        print(" ",end="")
    for k in range (i) :
        if i%2 == 0 : print("#",end="")
        else : print("*",end="")
        
    print("")

print("")

list = [1,2,3,4,5]
print(list[-2])


print("")

for i in range(1,6) :
    print(list[5-i],end="")