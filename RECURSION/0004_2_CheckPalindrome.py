def checkPalindrome(s, i, n):
    if i >= n - i - 1:
        return True
    elif s[i] != s[n - i - 1]:
        return False
    return checkPalindrome(s, i + 1, n)
s = input("Enter String to Check Palindrome: ")
print("Is String " + s + " a Palindrome: " + str(checkPalindrome(s, 0, len(s))))