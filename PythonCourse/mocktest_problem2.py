__author__ = 'Kalyan'

problem_notes = '''
This problem involves writing an iterator class that implements a CyclicCounter that take a value
and returns values descending down to 0 and then back to the value infinitely.

For e.g. for bound = 3. the iterator next() cycles through the values 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, ....

Notes:
- implement the methods of the class so that it behaves like an iterator with behavior described above
- a non positive value should raise ValueError
- no type checking required.
- you must use a constant amount of memory irrespective of the counter starting value (ie) I should be able to use
  really large values without running out of memory etc.
'''


class CyclicCounter(object):
    def __init__(self,bound):
        self.inc=1
        self.bound=bound
        self.value=bound
    def __iter__(self):
        return self
    def next(self):
        value=self.value
        if(self.bound==0):
            return 0
        if(self.value==0 or self.value==self.bound):
            self.inc=self.inc*-1
        self.value=self.value+self.inc
        return value
    pass
def getList(bound):
    if(type(bound).__name__!='int'):
        raise ValueError
    if(bound<0):
        raise ValueError
    c = CyclicCounter(bound)
    # test the 1st 5 values, write
    i = 0
    result = []
    while i < 5:
        result.append(c.next())
        i += 1
    return result
# a basic test is given, write your own tests.
def test_counter():
    c = CyclicCounter(2)
    # test the 1st 5 values, write
    i = 0
    result = []
    while i < 5:
        result.append(c.next())
        i += 1
    assert [2,1,0,1,2] == result
    try:
        assert [1,0,1,0,1]==getList(1)
        assert [0,0,0,0,0,]==getList(0)
        assert []==getList(-1)
    except ValueError:
        assert True



