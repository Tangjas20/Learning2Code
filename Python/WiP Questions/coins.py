amount = input("Enter a dollar amount: ")
denominations = [100,50,10,5,2,1]
d_tracker = [0,0,0,0,0,0]
try:
    amount = int(amount)
except:
    print("Invalid number")

while amount >= denominations[0]:
    amount -= denominations[0]
    d_tracker[0] += 1

while amount >= denominations[1]:
    amount -= denominations[1]
    d_tracker[1] += 1
    
while amount >= denominations[2]:
    amount -= denominations[2]
    d_tracker[2] += 1
    
while amount >= denominations[3]:
    amount -= denominations[3]
    d_tracker[3] += 1
    
while amount >= denominations[4]:
    amount -= denominations[4]
    d_tracker[4] += 1

while amount >= denominations[5]:
    amount -= denominations[5]
    d_tracker[5] += 1
    
print(d_tracker)
indexer = 0
for i in d_tracker:
    if i > 0:
        print("{} x ${}".format(i,denominations[indexer]))
    indexer+= 1