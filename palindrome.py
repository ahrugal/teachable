# Palindrome Checker

aword = "tacocat"
bword = "paris"

def palindrome(word):
    if word.lower() == word[::-1].lower():
        print ("Yes, " + word + " is a palindrome")
    else:
        print ("No, " + word + " is not a palindrome, " + word[::-1] + ", as you can see.")
