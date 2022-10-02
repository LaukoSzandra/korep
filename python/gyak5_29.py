import random
n=random.randint(1,50)


while True:
    tipp=int(input("Tipp: "))
    if(tipp==n):
        break
    elif(tipp<n):
        print("A gondolt szám nagyobb")
    else:
        print("A gondolt szám kissebb")
        