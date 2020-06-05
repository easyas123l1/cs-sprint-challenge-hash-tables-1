def intersection(arrays):
    """
    create a list of caches of each array.
    compare the first cache to all other 
    caches and find if #s exist in all other cache
    if so add to result 
    """
    result = []
    caches = []

    for i in range(len(arrays)):
        cache = {}
        for j in range(len(arrays[i])):
            cache[arrays[i][j]] = 1

        caches.append(cache)

    first = caches[0]
    rest = caches[1:]
    for key in first:
        add = True
        for cach in rest:
            if key not in cach:
                add = False
        if add:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
