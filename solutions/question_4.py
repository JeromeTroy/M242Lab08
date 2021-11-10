from sympy import Sum, log, oo, lambdify, log
from sympy.abc import k, n

# solving
from sympy.solvers import solve

# math log
import math

# defining series
a_k = 1 / (log(k) * 2**k)

# comparison with geometric series
# k > 2 => a_k < 1 / 2^k = r^k
# sum_{k=n+1}^oo r^k = r^{n+1} sum_{k=0}^oo r^k = r^{n+1} * 1 / (1 - r)
# therefore f(n) = 2^(-n)

# f(n) <= epsilon
# requires n >= -log_2(epsilon)
def compute_max_n(error):
    return -math.log(error) / math.log(2)

def compute_sum_within_error(error):
    required_n = int(compute_max_n(error)) + 1

    a_k_fun = lambdify(k, a_k)
    sum_value = sum(
            [a_k_fun(k_val) 
                for k_val in list(range(2, required_n))]
    )

    return sum_value

print("Testing")

errors = [1e-1, 1e-3, 1e-6, 1e-10, 1e-12, 1e-16]
sums = []
print("error \t sum_value")
print("------------------")

for error in errors:
    sum_value = compute_sum_within_error(error)
    sums.append(sum_value)
    print(error, "\t", sum_value)

print("allowed error \t actual error")
print("-----------------------------")
for index in range(len(sums)):
    print(errors[index], "\t\t", abs(sums[index] - sums[-1]))
