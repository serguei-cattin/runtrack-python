import random
L = []
list = (1,2,3,4,5,6,7,8,9,10)
for i in range(5):
    L.append(random.choice(list))
print(L[1])
L[3] = L[2]+L[4]
print(L[-1])
