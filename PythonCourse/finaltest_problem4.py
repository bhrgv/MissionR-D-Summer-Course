__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
 This is another custom encryption scheme that was in popular use to send secret messages in olden days. In this
 scheme successive letters are written in different lines by hand and all the characters are merged line by line
 to create the final encrypted text. The number of lines can differ and is an input to this problem.

 Write encode and decode routines for this cipher given a text and the number of lines n.

 E.g "Hello Cat" with line count 2 when written over 2 lines is:
line1:              H   l   o    C   t
line2:                e   l   ' '  a

    So final text is "HloCtel a" (characters of line 1 followed by characters of line2)

Similarly a word "Popular" with line count 3 will be
line1:            P       l
line2:              o   u   a
line3:                p       r

    So final text is Plouapr

Constraints and notes:
1. Write the cipher routines work for arbitrary n. Raise value error if n <= 0
2. Assume types are correct
3. Note that the encryption is not done word by word but for the whole text at one go. See the "Hello cat" example, the
   space was treated as part of text and it moved.
4. Make good use of python builtins and data structures. Note that successive characters will go into lines
   1, 2, 3, 2, 1, 2, 3, 2, 1, ... for n=3 (repeating pattern)
5. Note that you are writing a program to solve this, so you can just use plain code and additional data structures
   to solve this instead of finding mathematical patterns (that is also allowed :-) ).
'''

def encode(text, n):
    lines=[]
    for count in range(n):
        lines.append([])
    line_number=0
    inc=1
    for letter in text:
        lines[line_number].append(letter)
        line_number=line_number+inc
        if(line_number==0 or line_number==n):
            if(line_number==n):
                line_number=n-2
            inc=inc*-1
    result=""
    print lines
    for line in lines:
        result=result+("".join(line))
    return result
    pass

def decode(text, n):
    lines=[]
    letters=[]
    result=[]
    for count in range(n):
        lines.append(0)
        letters.append([])
    line_number=0
    inc=1
    for letter in text:
        lines[line_number]=lines[line_number]+1
        line_number=line_number+inc
        if(line_number==0 or line_number==n):
            if(line_number==n):
                line_number=n-2
            inc=inc*-1
    index=0
    line_number=0
    for count in lines:
        for counter in range(count):
            letters[line_number].append(text[index])
            index=index+1
        line_number=line_number+1
    index=0
    line_number=0
    inc=-1
    flag=0
    for count in range(len(text)):
        result.append(letters[line_number][index])

    print result
    pass


# write your own tests.
def test_encode():
    assert "Plouapr" == encode("Popular",3)
    print encode("Popularity",4)
    pass

def test_decode():
    decode("Plouapr",3)
    pass
