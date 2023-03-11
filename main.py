import random

user_input_minimum_value = int(input("Enter the minimum value for the random number generator: "))
user_input_maximum_value = int(input("Enter the maximum value for the random number generator: "))


def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)


def generate_fibonacci_sequence(maximum):
    sequence = [0, 1]
    while sequence[-1] < maximum:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence[:-1]


def count_odd_numbers(sequence):
    return len([x for x in sequence if x % 2 != 0])


maximum_value = generate_random_number(user_input_minimum_value, user_input_maximum_value)
fibonacci_sequence = generate_fibonacci_sequence(maximum_value)
odd_numbers_count = count_odd_numbers(fibonacci_sequence)

print(f"The random value generated is {maximum_value}.")
print(f"The Fibonacci sequence up to {maximum_value} is {fibonacci_sequence}.")
print(f"There are {odd_numbers_count} odd numbers in the Fibonacci sequence.")

