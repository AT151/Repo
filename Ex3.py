numlist = []
numofnum = int(input("Input number of numbers in your list: "))

for x in range(0,numofnum):
    num = input("Please enter a number: ")
    numlist.append(int(num))

numrep = 0
xnum = int(input("Enter the number you want to find: "))

for x in numlist:
    if x == xnum:
        numrep = numrep + 1

print("The number of times {0} is repeated is".format(xnum),numrep)


