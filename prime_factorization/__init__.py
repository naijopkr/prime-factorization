from get_prime_number import get_prime_number

def prime_factorization(number):
    prime_number = get_prime_number()
    factors = []

    quotient = number
    while quotient != 1:
        factor_candidate = next(prime_number)

        while quotient % factor_candidate == 0:
            factors.append(factor_candidate)
            quotient = quotient / factor_candidate

    return factors
