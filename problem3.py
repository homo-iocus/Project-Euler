#Problem 3 : https://projecteuler.net/problem=3

def trial_division(n: int) -> list:
    # Return a list of the prime factors for a natural number.
    a = []
    f = 2                # The first possible factor.
    while n > 1:         # While n still has remaining factors...
        if n % f == 0:   # The remainder of n divided by f might be zero.
            a.append(f)  # If so, it divides n. Add f to the list.
            n /= f       # Divide that factor out of n.
        else:            # But if f is not a factor of n,
            f = f + 1       # Add one to f and try again.
    return a

print(trial_division(600851475143))
