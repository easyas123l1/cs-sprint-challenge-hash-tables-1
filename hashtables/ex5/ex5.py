"""
    Plan turn file paths into file names by removing 
    all of string left to the last '/'.  Set the key in 
    cache to this shortened file name and the value to 
    an array with this filepath as string unless already 
    exist.  If exist we append the filepath.  Lastly we loop 
    thru all queries and if query is in cache we append
    all items into result.
    """


def finder(files, queries):
    result = []
    cache = {}
    for file in files:
        index = file.rindex('/')
        rest = file[index+1:]
        if rest in cache:
            cache[rest].append(file)
        else:
            cache[rest] = [file]
    for query in queries:
        if query in cache:
            for i in cache[query]:
                result.append(i)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
