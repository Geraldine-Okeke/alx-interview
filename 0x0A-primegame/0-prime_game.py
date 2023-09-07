#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def calculate_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = calculate_primes(n)
        num_primes = len(primes)

        if num_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Test the function with your example
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
