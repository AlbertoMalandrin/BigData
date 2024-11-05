# cicli while e for

import random

n=0
while not (n==7):
    n=random.randint(0,10)
    print(n, end="\n")

print("end")

n=0
while(n<10):
    print(n, end="")
    n+=1

for n in range(0,10):
    print(n, end=" ")

 
print("\nfor array: ")
numeri=[1,10,23,34,45,56]
for el in numeri:
        print(el, end=" ")

# break 
print("\nfor + break: ")
for n in range(0,10):
    if n==5:
         break
    print(n, end=" ")

# continue
print("\nfor + break: ")
for n in range(0,10):
    if n==5:
         continue
    print(n, end=" ")