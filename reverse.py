"""Reverse a string"""
N = input()
LSTR = []
RSTR = []
for i in N:
    LSTR.append(i)
for i in range(len(N)):
    RSTR.append(LSTR.pop())
NEW_STRING = "".join(RSTR)
print("New string is {}".format(NEW_STRING))
