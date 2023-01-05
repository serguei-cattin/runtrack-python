def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in range(2, 1000):
    if est_premier(n):
        print("Le nombre est Premier", n,"!")