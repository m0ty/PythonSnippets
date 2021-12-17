"""
A palindrome is a string that reads the same from the left and from the right. 
For example, mom and tacocat are palindromes, as are any single-character strings.  Given a string, 
determine the number of its substrings that are palindromes.

Example:
The string is s = 'tacocat'.
Palindromic substrings are ['t', 'a', 'c', 'o', 'c', 'a', 't', 'coc', 'acoca', 'tacocat'].
There are 10 palindromic substrings.
"""

def is_palindrome(word):
    if len(word)==0:
        return False
    elif len(word)==1:
        return True
    
    return word == word[::-1]

def palindrome_counter(word):
    counter = 0

    for i in range(len(word)):
        sub_word = word[i:]

        if is_palindrome(sub_word):
            counter +=1

        for j in range(len(sub_word)):
            if is_palindrome(sub_word[:-j]):
                counter +=1

    return counter

print(palindrome_counter("tacocat"))