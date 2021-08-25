# write an app that checks if a given string of characters can be rearranged into a palindrome
# example input: aaabbbb
# output: true

def check_palindrome(word):
    """Method to check if a string can be rearranged into a palindrome"""
    # creating an empty list to which we add the characters of the string
    characters_list = []
    # a variable to count the spaces in the string
    count_spaces = 0

    for character in word.lower():
        # if the character is already in our list, we remove it
        if character in characters_list:
            characters_list.remove(character)
        # if the character is a space, we ignore it and increment our variable
        elif character == ' ':
            count_spaces += 1
            continue
        # if it's not in our list, we add it
        else:
            characters_list.append(character)

    # if the length of the list is 0 and the length of the string is an even number
    # the string can be rearranged as a palindrome
    if len(characters_list) == 0 and (len(word)-count_spaces) % 2 == 0:
        return True

    # if the length of the list is 1 and the length of the string is an odd number
    # the string can be rearranged as a palindrome as well, but only 1 character repeats itself an odd number of times
    elif len(characters_list) == 1 and (len(word)-count_spaces) % 2 == 1:
        return True
    else:
        return False


string_to_be_checked = input('Please type here the string you want to check -> ')
print(check_palindrome(string_to_be_checked))
