"""Print fibo series"""
def fibo(NUM):
    A = 1
    B = 1
    S = B
    LIST = [A, B]
    while S < NUMBER:
        S = A+B
        A = B
        B = S
        if S > NUMBER:
            break
        LIST.append(S)
    return LIST
NUMBER = int(input())
if NUMBER==0:
    print(None)
else:
    print("Fibo series : {} ".format(fibo(NUMBER)))
