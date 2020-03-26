from get_prime_number import get_prime_number

def prime_factorization(number):
    prime_number = get_prime_number()
    factors = []

    rest = number
    while rest != 1:
        factor_candidate = next(prime_number)

        while rest % factor_candidate == 0:
            factors.append(factor_candidate)
            rest = rest / factor_candidate

    return factors
