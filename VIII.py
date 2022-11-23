"""

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

"""
import random

comp = random.randrange(1, 10)

while True:
    
    guess = int(input("guess the number."))
    

 
    print() 
    if comp == guess:
        print("indeed")
 
        break

    if comp < guess:
     print("it is less than your guess.")

    if comp > guess:
        print("it is greater than your guess.")