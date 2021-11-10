"""
Lab 08, questions 1 - 3
"""

# import plotting capabilities
import matplotlib.pyplot as plt

# import symbolic "k" which can be used to create symbolic expressions
from sympy.abc import k
# import symbolic summations and infinity (oo), and other important values
from sympy import Sum, oo, E, pi, lambdify, log, factorial

# a separate file
from sum_errors import compute_sum_errors

def partial_sum_general(a_k, n, sum_start=1):
    """
    Do a partial sum of the first n values of the series
    \sum 1 / k

    Input:
        a_k : form of the series term, e.g. a_k = 1 / k
            MUST BE A SYMPY EXPRESSION
        n : highest number in partial sum
    Output:
        partial_sum : sum of first n terms in series (assuming k starts at 1)
    """

    k_values = list(range(sum_start, n))
    # build a callable function
    a_k_function = lambdify(k, a_k)
    partial_sum = sum([a_k_function(k) for k in k_values])
    return partial_sum

def print_table(n_list, value_list, step):
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
    for index in range(0, len(n_list), step):
        print(n_list[index], "\t", value_list[index])

"""
Defining series, 
printing series values,
plot the sums of series,
evaluate exact sum of series
"""

a_k = 1 / k
n_values = list(range(100))
partial_sums_list = []
for n in n_values:
    partial_sums_list.append(partial_sum_general(a_k, n))

print_table(n_values, partial_sums_list, 10)

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

# create an expression for the sum
sum_expression = Sum(a_k, (k, 1, oo))
# perform operation
print("Sum value: ", sum_expression.doit())

"""
A second example
"""
b_k = 1 / (k**2)
exact = Sum(b_k, (k, 1, oo)).doit()
max_n_value = 50
starting_k_value = 1
partial_sum_errors = compute_sum_errors(exact, b_k, starting_k_value, max_n_value)

n_list = list(range(starting_k_value, max_n_value))
print_table(n_list, partial_sum_errors, 5)

"""
Questions for lab
"""

print("Question 1")

print("Part i) a_k = 1 / k^2")

a_k = 1 / k**2
n_values = list(range(100))
partial_sums_list = []
for n in n_values:
    partial_sums_list.append(partial_sum_general(a_k, n))

print_table(n_values, partial_sums_list, 10)

# plotting
plt.plot(n_values, partial_sums_list, ".")

# pretty up the plot
plt.xlabel("N")
plt.ylabel("$S_N$")

# set title
plt.title("Partial sums for $a_k = \\frac{1}{k^2}$")

# display the plot
plt.show()

# create an expression for the sum
sum_expression = Sum(a_k, (k, 1, oo))
# perform operation
print("Sum value: ", sum_expression.doit())

print("Part ii) a_k = (ln(k) / k)^2")

a_k = (log(k) / k)**2
n_values = list(range(100))
partial_sums_list = []
for n in n_values:
    partial_sums_list.append(partial_sum_general(a_k, n))

print_table(n_values, partial_sums_list, 10)

# plotting
plt.plot(n_values, partial_sums_list, ".")

# pretty up the plot
plt.xlabel("N")
plt.ylabel("$S_N$")

# set title
plt.title("Partial sums for $a_k = \\left(\\frac{\\ln k}{k}\\right)^2$")

# display the plot
plt.show()

# create an expression for the sum
sum_expression = Sum(a_k, (k, 1, oo))
# perform operation
print("Sum value: ", sum_expression.doit())


print("Part iii) a_k = 1 / k!")

a_k = 1 / factorial(k)
n_values = list(range(100))
partial_sums_list = []
for n in n_values:
    partial_sums_list.append(partial_sum_general(a_k, n, sum_start=0))

print_table(n_values, partial_sums_list, 10)

# plotting
plt.plot(n_values, partial_sums_list, ".")

# pretty up the plot
plt.xlabel("N")
plt.ylabel("$S_N$")

# set title
plt.title("Partial sums for $a_k = \\frac{1}{k!}$")

# display the plot
plt.show()

# create an expression for the sum
sum_expression = Sum(a_k, (k, 0, oo))
# perform operation
print("Sum value: ", sum_expression.doit())


