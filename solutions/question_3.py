from sympy import factorial, E, oo, Sum
from sympy.abc import k

import matplotlib.pyplot as plt

from sum_errors import compute_sum_errors

# build series and the exact solution
a_k = 1 / k**2
exact = float(Sum(a_k, (k, 1, oo)))

sum_start = 1
highest_n = 1000

errors_list = compute_sum_errors(exact, a_k, sum_start, highest_n)

n_values = list(range(sum_start, highest_n))

plt.loglog(n_values, errors_list)
plt.xlabel("N")
plt.ylabel("$\\epsilon_N$")
plt.title("Error for partial sums of $a_k = 1 / k^2$")

plt.show()

print("This is a much worse approximation, as 1000 terms only gets 3 digits of accuracy")
