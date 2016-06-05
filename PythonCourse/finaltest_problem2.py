__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
 For this problem, you will write simple infinite generators for primes and fibonacci numbers.

 In addition you will write a simple generator common_elements function which returns the
 intersection of 2 given sorted iterators/iterables

'''

# Returns a generator which returns the sequence of primes infinitely.
# returns 2, 3, 5, 7, 11, 13,  ... successively
def isPrime(num):
    for number in range(2,num):
        if(num%number==0):
            return False
    return True
def primes():
    number=2
    while True:
        while(True):
            if(isPrime(number)):
                break
            number=number+1
        yield(number)
        number=number+1
    pass

# Returns a generator which returns the sequence of fibonacci numbers infinitely
# 1, 1, 2, 3, 5, 8, 13, ... successively (note that you should start from 1, 1 and not 0, 1)
def fibonacci_numbers():
    a=0
    b=1
    while True:
        yield(b)
        a,b=b,a+b
    pass

# This is a generator which returns the common elements in both the first and second sorted iterators/iterables. If first
# and second are infinite, then this is also infinite. Assume that both first and second are sorted in ascending order.
# A simple use case for this is to find fibonacci numbers which are also primes using the two generators given above.
# It should work for any sorted iterator or iterable, so code accordingly.
#
# No special error checking required, allow errors to percolate up on wrong inputs.
def common_elements(seq1, seq2):
    past=[]
    while True:
        fib=next(seq1)
        while True:
            prime=next(seq2)
            past.append(prime)
            if fib == prime:
                temp=fib
                fib=next(seq1)
                yield(temp)
            elif fib in past:
                temp=fib
                fib=next(seq1)
                yield(temp)
            elif fib < prime:
                break
    pass


# write your own tests.
def test_primes():
    test_prime=primes()
    assert [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] == [next(test_prime) for count in range(15)]
    pass


def test_fibonacci():
    test_fibonacci=fibonacci_numbers()
    assert [1, 1, 2, 3, 5, 8, 13] == [next(test_fibonacci) for count in range(7)]
    pass

def test_common_elements():
    seq2=primes()
    seq1=fibonacci_numbers()
    seq=common_elements(seq1, seq2)
    [2, 3, 5, 13, 89, 233, 1597] == [next(seq) for count in range(7)]
    pass

