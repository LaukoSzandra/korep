from re import T


while True:
    a=int(input("a="))
    b=int(input("b="))
    if(a==b):
        break
    elif(a>b):
        print("a nagyobb mint b")
    else:
        print("b nagyobb mint a")