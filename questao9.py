import random

n = random.randint(1, 10)
y=0
while y < 3:
    y+=1
    x = int(input("Escolha um número entre 1 e 10:"))
    if (x == n):
        print("Você acertou!")
        exit(0)
    else:
        print("Você errou.")
print("Tente outra vez")
