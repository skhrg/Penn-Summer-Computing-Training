It's always great when your code works.

But then you try to scale it up, running on thousands of images instead of the five you started with, and you're stuck staring at a screen. You find out it will take hours and hours to run your program; oh no!

Let's figure out how to make our program faster, _without breaking it_, through an instructive example.

## The situation
Your advisor has given you a piece of code, and it's really slow. You will need to:
- Figure out what it does
- Figure out how it does that
- Figure out where it is slow
- Figure out how to improve the slow parts.
### The code
Here's the code your advisor gave you:
```python
#numerical integration

dx = 1.0 / 1000000

output_areas = []

x_cubes = [1, 8, 0.8, 3, 2.0, 77]

for i in range(len(x_cubes)):
    x = 0 
    while x < 1.0:
        x = x + dx / 2
        output_areas.append((x_cubes[i] * (x**3) +5*x**2 + 2*x + 5) * dx)
        x = x + dx / 2


    output = sum(output_areas)
    output_areas = []

    print(x_cubes[i], " gives output")
    print(output)
    print()
```
And you run it in your terminal...
```
$ python3 old_python_script.py 

1  gives output
7.91667966657

8  gives output
9.66668666645

0.8  gives output
7.86667946657

3  gives output
8.41668166653

2.0  gives output
8.16668066655

77  gives output
26.9167556653
```
Based on a quick reading of the code, you summise that this is likely a numerical integration script, that uses the rectangular rule!
![[Pasted image 20240610105218.png]]You can see that the variable `x_cubes` stores a bunch of pre-factors for the equation:
$$
{x\_cubes} \cdot x^3 + 5x^2 + 2x + 5
$$
And the loop is over independent integrations of this function.
## Source formatting
As we are going to be making changes to this code, we want to make sure that any changes we make are actually substantial and do not just change the way the code 'looks'. For instance, we could put a new line between all the `x_cubes`:
```python
x_cubes = [
	1,
	8,
	0.8,
	3,
	2.0,
	77
]
```
This makes the code look very different, but it behaves exactly the same. This example is a little contrived, but this is actually a huge problem when working under version control. You always want any differences between files to represent changes in the behaviour!

One way to enforce this is to use an automated source formatter. A great example of this for python is called `black` (see also `ruff`). Running `black our_script.py` will re-format it into a standard way. If you then edit it and change the formatting, running `black` will re-set it to the original standard!

```python
# numerical integration

dx = 1.0 / 1000000

output_areas = []

x_cubes = [1, 8, 0.8, 3, 2.0, 77]

for i in range(len(x_cubes)):
    x = 0
    while x < 1.0:
        x = x + dx / 2
        output_areas.append(
            (x_cubes[i] * (x ** 3) + 5 * x ** 2 + 2 * x + 5) * dx
        )
        x = x + dx / 2

    output = sum(output_areas)
    output_areas = []

    print(x_cubes[i], " gives output")
    print(output)
    print()
```

For our code, this placed a standard set of spaces between the `output_areas.append()` items.

We now have a standard platform to make changes on, and we know that any changes we see in the file may cause changes in the underlying execution of the code.
### Source code testing
Right now, the only way that we can 'test' our code is by running it and comparing it to previous runs. Let's say we do trust our advisor that the code currently works (rather than verifying the integrations by hand): this is not particularly repeatable and requires significant input from us every single time.
#### Code refactoring
Refactoring is a process where you do not change the output or input of the code, but change its internals and the way it is written. Just in the same way as you would re-write sections of a paper if it was unclear, why not do the same for code? Refactoring can both make code longer or shorter, depending on the situation. Code does not need to be short, it needs to be understandable and fast.

To make our code testable, we need to refactor the core into a function that we can call and compare against fixed outputs. Below, we've improved the code we were given by making some significant changes (documented inline!)

```python
from typing import List, Tuple

def solve_integrals(
    cube_prefactors: List[float], # Parameters have 'type hints'
    n_steps: int,
    integration_range: Tuple[float],
) -> List[float]:
    """
    Solves the integrals:

    [cube_prefactor] x^3 + 5x^2 + 2x + 5

    using the rectangle rule between the integration bounds given
    with n_steps rectangles. Returns a list of results, one for each
    of the cube_prefactors.
    """

    # Actual step size
    dx = (integration_range[1] - integration_range[0]) / n_steps

    # Returned at the end, same length as cube_prefactors
    integrals = []

    for i in range(len(cube_prefactors)):
        output_areas = []
        x = integration_range[0]
        while x < integration_range[1]:
            x = x + dx / 2
            output_areas.append(
                (cube_prefactors[i] * x ** 3 + 5 * x ** 2 + 2 * x + 5)
                * dx
            )
            x = x + dx / 2

        output = sum(output_areas)
        integrals.append(output)

    return integrals


if __name__ == "__main__":
	# Constants and functions are now in this block to only run
	# in script mode
    n_steps = 1_000_000
    integration_range = (0.0, 1.0)
    x_cubes = [1, 8, 0.8, 3, 2.0, 77]

    integrals = solve_integrals(x_cubes, n_steps, integration_range)

    for integral, cube in zip(integrals, x_cubes):
	    # f-strings provide a more helpful interface to printing and
	    # string formatting
        print(f"{cube} gives output\n{integral}\n")
```

We've made a number of changes:
1. Moved the core integration code into a function.
2. This function has the required parameters 'documented' with type hints: these hints tell you what variable types go into and out of the function.
3. We have added a docstring to our function to explain to the next person what's going on.
4. We've moved all of the 'script-mode' code to the `if __name__ == "__main__":` block, which only runs if the script is ran with `python3 my_script.py`, and is not ran when the script is imported from another one.
5. We used fstrings to do the printing.

Now our core code is in a function we can write, in a separate file, some code that tests it:

```python
from refactored_script import solve_integrals

import numpy as np

def test_integrals():
    n_steps = 1_000_000
    integration_range = (0.0, 1.0)
    x_cubes = [1, 8, 0.8, 3, 2.0, 77]

    integrals = solve_integrals(x_cubes, n_steps, integration_range)
    expected = [7.9166, 9.6666, 7.8667, 8.4166, 8.1667, 26.9167]

    assert np.isclose(integrals, expected, 0.001).all()

if __name__ == "__main__":
	# Not used by pytest, but useful for our profiling.
    test_integrals()
```

A test has three major components:
1. _Set-up_ of state required to run the function. In our case, this is the input parameters.
2. _Running_ the code you want to test, and getting results.
3. _Assertion_ against known results (here, what the code printed out before)

Note that we placed the test code in a function that is named `test_{something}`. We can run the tests with `pytest`, which is a testing framework for python. `pytest` looks for functions starting with the name `test`, and runs them, checking that they work correctly. If our test code is in `test_integration.py`, we can run:

```
$ pytest test_integration.py
============================= test session starts ==============================
platform darwin -- Python 3.7.3, pytest-4.3.0, py-1.8.0, pluggy-0.9.0
rootdir: /Users/mphf18/Documents/talks/st_andrews_2019, inifile:
collected 1 item                                                               

test_integration.py .                                                    [100%]

=========================== 1 passed in 2.99 seconds ===========================
```

This test is important for two main reasons: one, it allows us to make sure that the code is correct (try changing the code to something you know is wrong, for instance changing 5 to 3, and running the test; it will fail and complain). Two, it gives us something to benchmark to figure out how fast (or slow) our code is.

Without a fixed reference point like this, when we try to fix our code to make it faster we won't know whether we've broken it, or if we've accidentally made it slower!

We can get a very basic understanding of how long our code takes to run by using the unix `time` command:

```
$ time python3 test_integration.py 

...

real 	0m3.776s
user 	0m3.660s
sys     0m0.093s
```

This tells us that it took 3.776s to run our code. Now we have a base _benchmark_, we can try to improve it!
#### Our first attempt
So, you've been told that python lists are 'slow' and numpy arrays are 'fast'. The integration routine above makes heavy use of python lists, so let's try turning them into numpy arrays?

```python
# Actual step size
dx = (integration_range[1] - integration_range[0]) / n_steps

# Returned at the end, same length as cube_prefactors
integrals = []

# These are always the same size
# This has been changed to a numpy array!
output_areas = np.empty(n_steps, dtype=float)

for prefactor in cube_prefactors:
	for step in np.arange(n_steps):
		x = integration_range[0] + (step + 0.5) * dx
		output_areas[step] = (
			(prefactor * x ** 3 + 5 * x ** 2 + 2 * x + 5)
			* dx
		)

	# Use the numpy function
	output = np.sum(output_areas)
	integrals.append(output)

return integrals
```

This still passes when using pytest, so let's run our profile again:

```
time python3 test_integration.py 

...

real	0m22.282s
user	0m24.240s
sys	0m4.320s
```

Uh, did that just take almost ten times as long? Yes, it did...
### Sampling profilers
To get a deeper understanding of where and when we are spending time, we can use a very helpful tool called a 'profiler'. A very useful type of profiler is called a 'sampling profiler'. This stops your code every (n) milliseconds, and asks it which line it is on. By doing this thousands and thousands of times, your statistics knowledge should tell you that the number of times we stopped on a line should correlate with the amount of time spent there...

Using `py-spy` is very simple:

```
py-spy record -o profile.svg -- python test_integration.py
```

This will produce a file (profile.svg) that you can open in your browser. On MacOS, for instance, you could do `open -a Safari profile.svg`.

![[Screenshot 2024-06-10 at 12.05.46 PM.png]]

Our expensive lines are the following two:

```python
x = integration_range[0] + (step + 0.5) * dx
output_areas[step] = (
	(prefactor * x ** 3 + 5 * x ** 2 + 2 * x + 5)
	* dx
)
```

Figuring out why these are expensive requires a little more thought. Our top line here, which just sets `x`, seems like it should be super quick; it's just adding some numbers together. However, it uses _mixed types_: `step` is a `np.int64`, and `0.5` is a python float...

Mixed types, in any programming language, but especially python, are extremely dangerous. They require the creation of a new object for every call. Here, we:

1. Notice that we want to add a np.int64 to a python float
2. Decide to give the float preference
3. Create new object x, a python float
4. Do the expensive conversion from an integer to a float

The other problem is that this slow conversion is having to happen for every single loop item! 

We can fix two birds with one stone: have our array of `x`s be generated with the correct type to begin with, and avoid this whole explicit loop:

```python
# Actual step size
dx = (integration_range[1] - integration_range[0]) / n_steps

# Returned at the end, same length as cube_prefactors
integrals = []

# These are always the same size
x = (
	np.arange(n_steps, dtype=np.float32) + 0.5
) * dx + integration_range[0]

for prefactor in cube_prefactors:
	output_areas = (
		prefactor * x ** 3 + 5 * x ** 2 + 2 * x + 5
	) * dx
	output = np.sum(output_areas)
	integrals.append(output)

return integrals
```

Running this through our profile yet again leaves us with only one hot line:

![[Screenshot 2024-06-10 at 12.44.26 PM.png]]

which is the calculation of the output areas. Our one line, `prefactor * x ** 3 + 5 * x ** 2 + 2 * x + 5`, is taking up almost the entirety of our program's runtime!

We can make two micro-improvements here:
1. We can notice that we use the same powers of x in each and every loop.
2. We can remove arbritary exponents: computing `x ** 2` is more expensive than `x * x`

This gives us our final code:
```python
# Actual step size
dx = (integration_range[1] - integration_range[0]) / n_steps

# Returned at the end, same length as cube_prefactors
integrals = []

# These are always the same size
x = (
	np.arange(n_steps, dtype=np.float32) + 0.5
) * dx + integration_range[0]

x_squared = x * x
x_cubed = x_squared * x
poly = 5 * x_squared + 2 * x + 5

for prefactor in cube_prefactors:
	output_areas = prefactor * x_cubed + poly
	output = np.sum(output_areas) * dx
	integrals.append(output)

return integrals

```

This runs our benchmark in 0.277 seconds, a 15x improvement on our starting time. The flamegraph tells us that we actually improved this even more than we think, with our actual code taking up a TINY fraction of the runtime (most of the time is spent importing modules).

![[Screenshot 2024-06-10 at 12.50.43 PM.png]]

## Summary

We took some code that we knew was slow and made it faster. But the important thing to learn here was how:

1. We refactored the code into a known state that could be used for performance testing
2. We established correctness and performance tests
3. Then, and only then, did we make optimizations to the core code, guided by the profiles that we generated.
4. We confirmed that each of our improvements worked in turn.

It is _absolutely critical_ that you _never_ try to optimize the performance of code without having first profiled and correctness-tested it.

The full final code:
```python
# numerical integration

from typing import List, Tuple
from numpy import sum, arange, float32


def solve_integrals(
    cube_prefactors: List[float],
    n_steps: int,
    integration_range: Tuple[float],
) -> List[float]:
    """
    Solves the integrals:

    [cube_prefactor] x^3 + 5x^2 + 2x + 5

    using the rectangle rule between the integration bounds given
    with n_steps rectangles. Returns a list of results, one for each
    of the cube_prefactors.
    """

    # Actual step size
    dx = (integration_range[1] - integration_range[0]) / n_steps

    # Returned at the end, same length as cube_prefactors
    integrals = []

    # These are always the same size
    x = (
        arange(n_steps, dtype=float32) + 0.5
    ) * dx + integration_range[0]

    x_squared = x * x
    x_cubed = sum(x_squared * x) * dx
    poly = (5 * sum(x_squared) + 2 * sum(x) + 5) * dx

    for prefactor in cube_prefactors:
        output = prefactor * x_cubed + poly
        integrals.append(output)

    return integrals


if __name__ == "__main__":
    n_steps = 1_000_000
    integration_range = (0.0, 1.0)
    x_cubes = [1, 8, 0.8, 3, 2.0, 77]

    integrals = solve_integrals(x_cubes, n_steps, integration_range)

    for integral, cube in zip(integrals, x_cubes):
        print(f"{cube} gives output\n{integral}\n")
```