def get_indices_of_item_weights(weights, length, limit):
    # Your code here
    cache = {}
    for i in range(len(weights)):
        # find partner
        x = limit - weights[i]
        # if partner exist in cache
        if x in cache:
            # figure out which way tuple should respond
            if cache[x] > i:
                return [cache[x], i]
            else:
                return [i, cache[x]]
        # add to cache
        else:
            cache[weights[i]] = i
    # no matches exist return None
    return None


weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_4)

# should = 2, 6
