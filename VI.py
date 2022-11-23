tal = [3, 19, 1, 27, 4, 55, 27]

def sort(tal):
    sorted = True

    while sorted:
        sorted = False
        for i in range(len(tal)):
            for j in range(len(tal) - 1):
                if tal[j] > tal[j + 1]:

                    tal[j], tal[j + 1] = tal[j + 1], tal[j]
                    sorted = True

    return tal


tal = sort(tal)
print(tal)
