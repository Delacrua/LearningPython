"""The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a
value, determine the number of each item to include in a collection so that the total weight is less than or equal to
a given limit and the total value is as large as possible.
complexity:
- exhaustive search - O(2 ** n)
- greedy algorithm - worst case O(n ** 2) - but does not guarantee optimal results
- dynamic programming algorithm - O(n * m) where n is number of items and m is limit of knapsack
"""
test_capacity = 10
test_weights = [3, 3, 3, 5, 4, 2, 4]
test_prices = [40, 40, 60, 50, 40, 20, 50]
items_number = len(test_weights)
"""
Case 1: exhaustive search
We try every available combination of items and choose the most valuable
"""


def pack_exhaustive(n, capacity, weights, prices):
    """
    The function solves knapsack problem using exhaustive search
    :param n: number of items left
    :param capacity: capacity of knapsack
    :param weights: weights of items
    :param prices: prices of items
    :return: max value of items fitting into capacity
    """
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return pack_exhaustive(n - 1, capacity, weights, prices)

    else:
        return max(prices[n - 1] + pack_exhaustive(n - 1, capacity - weights[n - 1], weights, prices),
                   pack_exhaustive(n - 1, capacity, weights, prices)
                   )


print('Packing with exhaustive algorithm')
print(pack_exhaustive(items_number, test_capacity, test_weights, test_prices))

"""
Case 2: greedy search
We try to pack items one by one starting with the most valuable one until we are out of capacity or items run out
"""


def pack_greedy(capacity, weights, prices):
    """
    The function solves knapsack problem using greedy search
    :param capacity: capacity of knapsack
    :param weights: weights of items
    :param prices: prices of items
    :return: max value of items fitting into capacity
    """
    total_price = 0
    items = list(zip(weights, prices))
    for i in sorted(items, key=lambda x: x[1], reverse=True):
        if capacity == 0:
            break
        if i[0] <= capacity:
            capacity -= i[0]
            total_price += i[1]
    return total_price


print('Packing with greedy algorithm')
print(pack_greedy(test_capacity, test_weights, test_prices))

"""
Case 3: dynamic programming 
"""


def pack_dynamic(capacity, weights, prices):
    """
    The function solves knapsack problem using dynamic programming
    :param capacity: capacity of knapsack
    :param weights: weights of items
    :param prices: prices of items
    :return: max value of items fitting into capacity
    """
    items_quantity = len(weights)
    knapsack = [[0] * (items_quantity + 1) for _ in range(capacity + 1)]
    for i in range(1, items_quantity + 1):
        for k in range(1, capacity + 1):
            if weights[i - 1] <= k:
                knapsack[k][i] = max(
                    knapsack[k][i - 1],
                    prices[i - 1] + knapsack[k - weights[i - 1]][i - 1]
                )
            else:
                knapsack[k][i] = knapsack[k][i - 1]
    return knapsack[capacity][items_quantity]


print('Packing with dynamic algorithm')
print(pack_dynamic(test_capacity, test_weights, test_prices))