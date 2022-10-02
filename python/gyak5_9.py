def f9():
    m=int(input("összeg: "))
    c=0
    while m>=200:
        m-=200
        c+=1
    print(f"{c}db 200Ft")
    c=0
    while m>=100:
        m-=100
        c+=1
    print(f"{c}db 100Ft")
    c=0
    while m>=50:
        m-=50
        c+=1
    print(f"{c}db 50Ft")
    c=0
    while m>=20:
        m-=20
        c+=1
    print(f"{c}db 20Ft")
    c=0
    while m>=10:
        m-=10
        c+=1
    print(f"{c}db 10Ft")
    c=0
    while m>=5:
        m-=5
        c+=1
    if m>0:
        c+=1
    print(f"{c}db 5Ft")

f9()