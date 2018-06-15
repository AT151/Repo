# n="*"
# for l in range(10):
#     print(n)
#     n = n +"**"

for i in range(10):
    for j in range(10):
        if j >= 10 - i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



