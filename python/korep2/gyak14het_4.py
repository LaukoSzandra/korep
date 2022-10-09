def main():
    f1()
    f2()
    f3()

def f1():
    a=int(input("alap: "))
    k=int(input("kitevő: "))
    e=a**k
    print(e)

def f2():
    a=int(input("alap: "))
    k=int(input("kitevő: "))
    for i in range(1, k+1):
        e=a**i
        print(f"{a}^{i}={e}")

def f3():
    a=int(input("alap: "))
    k=int(input("kitevő: "))
    if(k!=0):
        e=a**k
        print(e)
    elif(k==0):
        print(1)




main()