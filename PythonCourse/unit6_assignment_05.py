__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by spaces. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    try:
        index=sentence.index("either")
        eindex=index
        if(index==0):
            return sentence
        elif sentence[index-1]!=' ' or sentence[index+6]!=' ':
            return sentence
        index=sentence.index("or",index+6)
        if sentence[index-1]!=' ' or sentence[index+2]!=' ':
            return sentence
        letter=[]
        x=0
        while x in range(index-1):
            if x==eindex:
                x=x+7
            letter.append(sentence[x])
            x=x+1
        print letter
        letter="".join(letter)
        print letter
        return letter
    except Exception:
        return sentence
    pass
def test_prune_either_or_student():
    assert "we could go to a movie" == prune_either_or("we could either go to a movie or a hotel")
    assert "we could either go to a movie else a hotel" == prune_either_or("we could either go to a movie else a hotel")
    assert "we could go to a movie" == prune_either_or("we could go to a movie")
    assert "either go to a movie or a hotel" == prune_either_or("either go to a movie or a hotel")
    assert "It is neither here nor there" == prune_either_or("It is neither here nor there")
    assert "Two mythical cities eitheron and oregon" == prune_either_or("Two mythical cities eitheron and oregon")
    assert None == prune_either_or(None)
    pass


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_prune_either_or(prune_either_or)
