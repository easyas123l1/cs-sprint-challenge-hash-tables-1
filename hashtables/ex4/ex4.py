def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for x in a:
        if x != 0:
            if x in cache:
                cache[x] += 1
            else:
                cache[x] = 1
                opposite = x * -1
                if opposite in cache:
                    if opposite > x:
                        result.append(opposite)
                    else:
                        result.append(x)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

result = has_negatives([-1, -2, 1, 2, 3, 4, -4])
result.sort()
# print(result)
# self.assertTrue(result == [1, 2, 4])

a = list(range(5000000))
a += [-1, -2, -3]

result = has_negatives(a)
result.sort()
# self.assertTrue(result == [1,2,3])
