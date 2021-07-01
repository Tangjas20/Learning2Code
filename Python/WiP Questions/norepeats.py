import sys

temp = []
duplicate = False
while duplicate == False:
    n = input("Give me an input: # ")
    j = 1
    print("hi")
    while j <= len(temp+1):
        print('yes')
        if n == temp[j]:
            print("Input number {} is not unique!".format(n))
            duplicate == True
        temp.append(n)
        j+=1
        print(j)

