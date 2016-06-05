__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
You're given a text file containing names of movie actors and films they've acted in - delimited
by comma followed by space.

Format:
{actor name}, {movie name 1}, {movie name 2}, {movie name 3}

Input:
File containing movies info and a number 'n', which represents the number of lines from top of file.

Output:
For each actor in the first n lines, you must return the chemistry record with 
the co-actor with which they have most movies in common.

So you have to return a maximum of n records (if every actor has someone he has worked with in the records).
In the case where no actors have any common movies, you return 0 records.

Example:
if a1 and a2 have c1 as common movie
and a1 and a3 have c1, c2, c3
and a1 has no common movies with any other actor, then you must return [a1, a3, [c1, c2, c3]] as the
max chemistry record for a1.

If a given actor has same count of common movies with multiple co-actors, choose the
first one in alphabetical order.

If a given actor has no common movies with any other, then do not emit any chemistry record for that actor.

Notes:
1. See if you can decompose this problem into meaningful subroutines.
2. Submit the movies.txt file into dropbox too. ** Do not modify the movies.txt file! **

'''
import inspect
import os

# represents the chemistry between two actors and the common movies between them.
# movies is a set of common movies, the actor and co_actor are name strings
class Chemistry(object):
    def __init__(self, actor, co_actor, movies):
        if not actor: raise ValueError("actor is not valid name")
        if not co_actor: raise ValueError("co-actor is not valid name")

        self.actor = actor
        self.co_actor = co_actor
        self.movies = movies

    def __hash__(self):
        return hash(self.actor)

    def __eq__(self, other):
        return (self.actor == other.actor) \
            and (self.co_actor == other.co_actor) \
            and (self.movies == other.movies)

    def __repr__(self):
        return str((self.actor, self.co_actor, self.movies))


# returns a set of Chemistry objects that represent the max chemistry of each actor.
# It is as if the file has only first n lines.
# Important: Use the helper routine given (open_input_file) to open the file to open the file which should
# be in same directory as this file.
def actors_chemistry(input_file, n):
    file=open_input_file(input_file)
    lines = file.readline()
    count = 0
    for count in range(n):
        line = lines[count]
        words=line.split(', ')
        actor=dict((words[0],words[1:]))
    pass


def test_actors_chemistry():
    assert {Chemistry('Leonardo Di Caprio', 'Tom Hardy', {'Inception', 'The Revenant'}),
            Chemistry('Tom Hardy', 'Leonardo Di Caprio', {'Inception', 'The Revenant'})} == actors_chemistry('movies.txt', 5)

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)