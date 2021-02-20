def h(k, i):
    return (h_tag(k) + i + (3 * i) ** 2) % 100


def h_tag(k):
    return k % 100


def hash_insert(t, k):
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
