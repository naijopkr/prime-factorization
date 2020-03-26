from prime_factorization import prime_factorization

def main():
    while True:
        try:
            number = int(input('Insert the number to be factored in prime numbers: '))
            if number <= 1:
                raise ValueError
        except ValueError or TypeError:
            print('Invalid number. Please, try again.')
        else:
            print(prime_factorization(number))
            if input('Wanna try again? (Y/n): ').lower() == 'n':
                break

if __name__ == '__main__':
    main()
