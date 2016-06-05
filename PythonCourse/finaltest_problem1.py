__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''

def smallest_palindrome(word):
    if type(word).__name__ !='str':
        raise TypeError
    import string
    unwanted=list(string.punctuation)
    for letter in word:
        if letter in unwanted:
            raise ValueError
    letters=list(word)
    index=0
    while index < len(letters)-1:
        if(letters[index].lower()==letters[-1].lower()):
            break
        index=index+1
    index=index-1
    while(index>=0):
        letters.append(letters[index].lower())
        index=index-1
    result="".join(letters)
    return result
    pass

# write your own tests
def test_smallest_palindrome():
    try:
        assert "Malayalam"==smallest_palindrome("Malayal")
        assert "Don't nod"==smallest_palindrome("Don't")
        assert "Steets"==smallest_palindrome("Ste")
        assert "Ap pa"==smallest_palindrome("Ap ")
        assert ""==smallest_palindrome(134)
        assert "134431"==smallest_palindrome("134")
    except ValueError:
        assert True
    except TypeError:
        assert True
    pass


