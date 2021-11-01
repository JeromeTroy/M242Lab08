"""
Example series analysis in Python
"""

# import plotting capabilities
import matplotlib.pyplot as plt

# import symbolic "k" which can be used to create symbolic expressions
from sympy.abc import k
# import symbolic summations and infinity (oo), and other important values
from sympy import Sum, oo, E, pi

def partial_sum(n):
    """
    Do a partial sum of the first n values of the series
    \sum 1 / k
    
    Input:
        n : highest number in partial sum
    Output:
        partial_sum : sum of first n terms in series (assuming k starts at 1)
    """
    
    k_values = list(range(1, n))
    partial_sum = sum([1 / k for k in k_values])
    return partial_sum

def print_table_sum(n_values, sum_values, step):
    """
    Print a pretty table of n values and partial sum values
    
    Input:
        n_values : list of values of n, the number of terms in each partial sum
        sum_values : list of partial sum values, corresponding to each n_value
        step : step size for how many to print, e.g. step = 10 means only print every 10th entry
    Output:
        No return value, instead prints a table
    """
    
    # table header
    print("n \t sum to n")
    print("-------------------")
    for index in range(0, len(n_values), step):
        print(n_values[index], "\t", sum_values[index])
        
"""
Generating example data
"""
n_values = list(range(100))
partial_sums_list = []
for n in n_values:
    partial_sums_list.append(partial_sum(n))
    
print_table_sum(n_values, partial_sums_list, 10)

# plotting
plt.plot(n_values, partial_sums_list, ".")

# pretty up the plot
plt.xlabel("n")
plt.ylabel("s(n)")

# display the plot
plt.show()

"""
Direct evaluation of series
"""
a_k = 1 / k
# create an expression for the sum
sum_expression = Sum(a_k, (k, 1, oo))
# perform operation
print("Sum value: ", sum_expression.doit())
    