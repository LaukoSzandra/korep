import random


while True:
    n=random.randint(1,12)
    print(n, n%3, sep=' ')
    m=chr(ord(input("Új szám? (i/n) ")))
    if m=='n':
        break