"""Check wheather a number is Prime or not and print all the prime numbers below that number"""
def prime(n_n):
    """Returns 1 or 0"""
    if n_n == 1:
        return 1
    for i in range(2, int(n_n/2)+1):
        if n_n%i == 0:
            return 1
    return 0
NU = int(input())
NUM = prime(NU)
if NUM == 0:
    print("Number is prime.")
else:
    print("Number is not prime.")
for a in range(2, NU+1):
    if prime(a) == 0:
        print("{}".format(a))
        