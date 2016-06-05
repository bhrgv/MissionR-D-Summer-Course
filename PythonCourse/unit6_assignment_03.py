__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if(type(first).__name__!='str' or type(second).__name__!='str'):
        return False
    if(len(first)!=len(second)):
        return False
    first_list=[x for x in first.lower()]
    second_list=[x for x in second.lower()]
    for x in first_list:
        if x in second_list:
            index=second_list.index(x)
            second_list[index]=None
        else:
            return False
    else:
        return True
    pass


# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip")
    assert True == are_anagrams("arrow", "rowra")
    assert False == are_anagrams("pit", "top")
    assert False == are_anagrams(None, None)
    assert False == are_anagrams(None, "hello")
    assert False == are_anagrams("hello", None)
    assert False == are_anagrams("bigg", "big")
    assert True == are_anagrams("Pit", "Tip")#sample test.


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_are_anagrams(are_anagrams)
