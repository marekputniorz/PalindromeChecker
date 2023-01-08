def isPalindrome(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    return False

programRun = True
while(programRun):
    palindrome = input("Enter string to test for palindrome or 'exit': ")
    if palindrome == 'exit':
        programRun = False
        break

    palindrome = palindrome.lower()

    newPalindrome = ""
    for x in palindrome:
        if x.isalnum():
            newPalindrome += x

    print("Palindrome test:", isPalindrome(newPalindrome))