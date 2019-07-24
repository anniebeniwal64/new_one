a=1
b=1
print(a)
print(b)
while(a<10):
    s=a+b
    a=b
    b=s
    print("fibonacci series{} ".format(s))
    