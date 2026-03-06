import random
import time


# gets price to price changes
def price_changes(prices):
    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i-1])
    return changes


# brute force code
def brute_force(arr):
    max_sum = float('-inf')
    start = end = 0
    iterations = 0

    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            iterations += 1

            if current_sum > max_sum:
                max_sum = current_sum
                start = i
                end = j

    return max_sum, start, end, iterations


# div and conq code

recursion_counter = 0

def max_crossing(arr, low, mid, high):

    left_sum = float('-inf')
    total = 0
    max_left = mid

    for i in range(mid, low-1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    total = 0
    max_right = mid+1

    for j in range(mid+1, high+1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return left_sum + right_sum, max_left, max_right


def divide_conquer(arr, low, high):
    global recursion_counter
    recursion_counter += 1

    if low == high:
        return arr[low], low, high

    mid = (low + high)//2

    left_sum, l_low, l_high = divide_conquer(arr, low, mid)
    right_sum, r_low, r_high = divide_conquer(arr, mid+1, high)
    cross_sum, c_low, c_high = max_crossing(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, l_low, l_high
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, r_low, r_high
    else:
        return cross_sum, c_low, c_high


# dyn prog code

def kadane(arr):

    max_sum = arr[0]
    current_sum = arr[0]

    start = end = s = 0
    iterations = 0

    for i in range(1, len(arr)):

        iterations += 1

        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

    return max_sum, start, end, iterations


# table code
def print_table(prices, changes):

    print("\nDay Index:")
    for i in range(len(prices)):
        print(f"{i:4}", end=" ")

    print("\nPrices:")
    for p in prices:
        print(f"{p:4}", end=" ")

    print("\nChanges:")
    print("    ", end=" ")
    for c in changes:
        print(f"{c:4}", end=" ")

    print("\n")



def run_algorithms(prices):

    changes = price_changes(prices)

    print_table(prices, changes)

    # brute force output
    start_time = time.time()
    max_sum, i, j, iterations = brute_force(changes)
    end_time = time.time()

    print("Brute Force")
    print("i =", i, " j =", j)
    print("Max profit =", max_sum)
    print("Iterations =", iterations)
    print("Time =", end_time-start_time)
    print()


    # div and conq output
    global recursion_counter
    recursion_counter = 0

    start_time = time.time()
    max_sum, i, j = divide_conquer(changes, 0, len(changes)-1)
    end_time = time.time()

    print("Divide & Conquer")
    print("i =", i, " j =", j)
    print("Max profit =", max_sum)
    print("Recursions =", recursion_counter)
    print("Time =", end_time-start_time)
    print()


    # dyn progr output
    start_time = time.time()
    max_sum, i, j, iterations = kadane(changes)
    end_time = time.time()

    print("Dynamic Programming")
    print("i =", i, " j =", j)
    print("Max profit =", max_sum)
    print("Iterations =", iterations)
    print("Time =", end_time-start_time)
    print()


# given data here
prices1 = [
100,113,110,85,105,102,86,63,
81,101,94,106,101,79,94,90,97
]

print("The 17 days data: ")
run_algorithms(prices1)


# 100 random days here
prices2 = [random.randint(50,120) for _ in range(100)]

print("\n\nThe random 100 days: ")
run_algorithms(prices2)