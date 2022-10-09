while True:
    n=int(input("Kérek egy számot 1-7 között: "))
    if(1<=n<=7):
        if(n==1):
            print("hétfő")
        elif(n==2):
            print("kedd")
        elif(n==3):
            print("szerda")
        elif(n==4):
            print("csütörtök")
        elif(n==5):
            print("péntek")
        elif(n==6):
            print("szombat")
        else:
            print("vasárnap")
        break