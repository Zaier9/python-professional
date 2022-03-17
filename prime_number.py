def is_prime(number: int) -> bool:
    #Return True if number is prime o False is not prime
    result_list = [x for x in range(2, number) if number % x == 0]
    return len(result_list) == 0


def run():
    number: int = 73
    number_is_prime: bool = is_prime(number)
    print(f'Is {number} a prime number? {number_is_prime}')


if __name__ == '__main__':
    run()