from sympy.abc import k
from sympy import lambdify

def compute_sum_errors(exact_value, a_k, sum_start, highest_n):
    """
    Compute the errors between the partial sum, and its exact value
    
    Input:
        exact_value : exact numerical value for the infinite sum
        a_k : Sympy expression for the k'th term in the sum
        n_start : starting k value for sum, usually either 0 or 1
        highest_n : maximum stopping value for sum
    Output:
        errors_list : list of errors of the partial sums
    """
    
    errors_list = []
    a_k_fun = lambdify(k, a_k)
    for max_n_value in range(sum_start, highest_n):
        # TODO: fill in what should be assigned to the error list
        partial_sum = sum(
                [a_k_fun(k_val) 
                    for k_val in list(range(sum_start, max_n_value))]
        )

        new_error = abs(partial_sum - exact_value)
        errors_list.append(new_error)
        
    return errors_list
