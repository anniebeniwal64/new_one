"""Print fibo series"""
NUMBER = int(input())
A = 1
B = 1
print(A)
print(B)
S = B
LIST = [A, B]
while S < NUMBER:
    S = A+B
    A = B
    B = S
    if S > NUMBER:
        break
    LIST.append(S)
print("Fibo series : {} ".format(LIST))
