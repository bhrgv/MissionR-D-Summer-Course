__author__ = 'Kalyan'

profiling_cprofile = '''
This is the tool of choice for analyzing large programs (parallel to the debugger). The profiler adds its own overhead
but for relative comparison of time spent, it is very very useful.

http://pysnippet.blogspot.in/2009/12/profiling-your-python-code.html
http://docs.python.org/2/library/profile.html in particular http://docs.python.org/2/library/profile.html#instant-user-s-manual

In particular, make sure you learn how to use pstats and running cProfile from command line as described in the
first post using a sample program before doing this assignment.

python -m cProfile [-o output_file] [-s sort_order] myscript.py

For this assignment learn to use the cProfile and pstats modules from the command line.
1. run the cprofile and collect a stats file
2. learn to use the stats file separately.
3. bypass the stats creation and directly print the output to console.

compare the cumulative times of these methods and then calculate per call times.
'''

from unit7_conversion_methods import *
#invoke each of the 4 methods 5 times in a loop for count=10000. Then run this in the profiler.
def profile_profiler():
    func=[numbers_string1,numbers_string2,numbers_string3,num_strings4]
    for x in func:
        time_list=[]
        for y in range(5):
            x(1000)
    pass


# compare the times taken per call using this method to what you found in the previous methods.
# when would you use the profiler over other methods, what additional data did you get from the profiler easily
# that would have taken more work in other methods?

# what did you learn about cProfile and pstats?

summary = '''
Time taken per call is same as given by the above methods(In timeit just for executing setup)
Profiler would be benifical for large Program mostly involved with more number of function calls
cProfile and pstats are usefull to anaylse the whole execution.
'''

if __name__ == "__main__":
    profile_profiler()
