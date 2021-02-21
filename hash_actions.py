def h(k, i):
    # Open addressing function receives the user id / book id and the parameter 'i' which will grow in case slot is
    # already taken
    return (h_tag(k) + i + (3 * i) ** 2) % 100


def h_tag(k):
    return k % 100


def hash_insert(t, k):
    # hash insert algorithm as per learning book, receives the users/books array and the id and returns an open slot to
    # populate. complexity is O(1)
    i = 0
    while i < len(t):
        j = h(k, i)
        if t[j] is None:
            t[j] = k
            return j
        else:
            i = i + 1
    print("hash overflow")


def hash_search(t, k):
    # hash search algorithm as per learning book, receives the users/books array and the id and returns the index where
    # the value is found. complexity is O(1)
    i = 0
    while i < len(t):
        j = h(int(k), i)
        if t[j] is not None:
            if t[j][0] == k:
                return j
            else:
                i = i + 1
        else:
            i = i + 1
    return
