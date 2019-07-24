"""Number is palindrome or not"""
def pali(s_t):
    """Print result"""
    new = s_t[::-1]
    if new == s_t:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
STRING = input()
pali(STRING)
