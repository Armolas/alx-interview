#!/usr/bin/python3
""" Prime game"""


def sieve(max_n):
    """Generate a list of primes up to
    max_n using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p, prime in enumerate(is_prime) if prime]
    return primes


def prime_game(n, primes):
    """Simulate one round of the prime game."""
    # Initially, all numbers from 1 to n are available
    available = [True] * (n + 1)
    available[0] = False  # No number 0 in the set
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        # Find the next prime number that is still available
        move_made = False
        for p in primes:
            if p > n:
                break
            if available[p]:
                # Make the move: remove p and all multiples of p
                move_made = True
                for multiple in range(p, n + 1, p):
                    available[multiple] = False
                break
        if not move_made:
            # No move can be made, current player loses
            return turn ^ 1
        turn ^= 1  # Switch turns


def isWinner(x, nums):
    """Determine the winner of the most rounds."""
    if not nums or x == 0:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n, primes)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
