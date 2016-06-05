__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).
'''

def left_binary_search(input, value):
    if type(input).__name__ != 'list':
        return -1
    index=-1
    low=0
    high=len(input)-1
    while(low<=high):
        mid=(low+high)/2
        if(input[mid]==value):
            index=mid
            high=mid-1
        elif input[mid]>value:
            high=mid-1
        else:
            low=mid+1
    return index
    pass

# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert 0 == left_binary_search([1,1,1,1,1,1,1],1)
    assert 5 == left_binary_search([1,3,4,5,6,7,7,9],7)
    assert -1 == left_binary_search(None,5)
    assert -1 == left_binary_search('string','s')
    assert -1 == left_binary_search([1,2,3],5)
    pass


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_left_binary_search(left_binary_search)
