$ python3 steps.py

1. Run steps.py using python3 (e.g., "python3 steps.py" within the terminal)

2. Check the terminal for a prompt, enter the number of steps that can be climbed. Do not enter a numebr less than 0.

3. Check the terminal for the total number of ways you could climb to the top. 

Method:
I approached this problem much like I would a bottoms-up fibonnaci sequence algorithm. In other words, I used dynamic programming w/ a bottoms-up approach. I received the output that I did because, as A increased, so there are a very large number of ways to get to the top - the total number ways to climb to step 55, depends on the total number to climb to step 54, 53,  .... 1. This is why the problem is very similar to how the fibonacci sequence is solved. 

The base cases, given that this is a bottoms up approach, are steps 1 and 2 - at step 1, we can only climb one way (one step). With 2 steps, we could climb by making one big step or two small steps. Each subsequent step then builds from these two. 