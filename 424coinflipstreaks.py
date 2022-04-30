import random
numberOfStreaks = 0
coin = []
counter = 0

for flips in range(9):
    flip = random.randint(1,2)
    if flip == 1:
        coin.append("H")
    elif flip == 2:
        coin.append("T")

for i in range(1,len(coin)):
    if coin[i] == coin[i-1]:
        counter+=1
    else:
        counter=0
    if counter == 2:
        numberOfStreaks+=1

print(coin)
print(numberOfStreaks)
print(counter)
