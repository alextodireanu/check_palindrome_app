# an app that checks if a given word is a palindrome

# first method using a reversed string
def check_palindrome(word):
    """Method to validate if a word is a palindrome"""
    if word == word[::-1]:
        return True
    else:
        return False


word_to_be_checked = input('Please type the word you want to check -> ')
print(check_palindrome(word_to_be_checked))


# second method using a for loop
def check_palindrome(word):
    """Method to validate if a word is a palindrome"""
    # first we find the middle of the string
    middle = int(len(word)/2)
    # reading the first half of the string and comparing it with the other half
    for i in range(middle):
        if word[i] != word[len(word)-i-1]:
            return False
    return True


word_to_be_checked = input('Please type the word you want to check -> ')
print(check_palindrome(word_to_be_checked))
