__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """

    if type(number).__name__ != 'int' or type(base).__name__ != 'int':
        raise TypeError
    elif base <=1 or base >36:
        raise ValueError
    import string
    result=[]
    symbols=list(string.uppercase)
    x=0
    flag=False
    if number<0:
        number=abs(number)
        flag=True
    while number!=0:
        x=number%base
        number=number/base
        result.append(x)
    result.reverse()
    for x in range(0,len(result)):
        digit=result[x]
        try:
            index=digit-10
            if index < 0:
                raise IndexError
            result[x]=symbols[index]
        except IndexError as ie:
            result[x]=str(digit)
    if flag:
        result.insert(0,'-')
    return "".join(result)
def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print te