L = [8, 24, 27, 48, 2, 16, 9, 102, 84, 91]
max = 0
min = 1000
for i in range(9):
    if L[i]> max:
        max= L[i]
    if L[i]< min:
        min = L[i]
print("Le minumum est de", min,"!")
print("Le maximum est de", max, "!")