# Travelbag
# Skelettkod till uppgiften

travelbag = ["Stand arrows", "Dragon", "Scissors", "Mohammed", "Saitama", "Kakarrot", "Joseph Joestar", "Hamon", "Dio"]

while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program")

   if menyval == "1":
       print(travelbag)

   elif menyval == "2":
      B = input ("what do you wish to put?").capitalize()
      travelbag.append(B)
      print(travelbag)


   elif menyval == "3":
    C = input ("What do you wish to remove?").capitalize()
    travelbag.remove(C)
    print(travelbag)

   elif menyval == "4":
       break