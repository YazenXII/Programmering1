score = 0

A = input ("France , capital?"). lower()
if A == ("paris"):
    print ("correct")
    score +=2

else: print ("Incorrect")

B = input ("Germany, Capital?"). lower()
if B == ("berlin"):
    print ("correct")
    score +=3

    print ("your score is", score)
    print("difficulty increase. Level medium")

    C = input ("what is known to be the biggest explotion in the universe?"). lower()
    if C == ("super nova"):
        print ("correct")
        score +=10
D = input ("what gas does exhaust out of humans?"). lower()
if D == ("CO2"):
    print("correct")
    score +=4

print ("your score is", score)
print ("difficulty increase. Level Hard")

print ("A. Billie Eilish\n B. Juice WRLD\n C. Travis Scott")
answer = input ("who got robbed of their grammys in 2019?"). lower()

if answer == ("travis scott") or answer ("C"):

    print ("correct")
    score += 12
