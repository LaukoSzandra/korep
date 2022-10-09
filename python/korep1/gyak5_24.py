while True:
    n=int(input("Kérek egy számot: "))
    if(n%3==0 and n%5==0):
        print(n/3, n/5, sep=' ')
        break
