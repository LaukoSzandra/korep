a = int(input("a="))
b = int(input("b="))
l = int(input("lépésköz: "))
s = ""

if (a > b):
    l = -l

s += str(a)
while a != b:
    a += l
    s += ", "+str(a)

print(s)