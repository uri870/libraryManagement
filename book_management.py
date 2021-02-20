import user_management
import hash_actions


def hash_search(t, k):
    i = 0
    while i < len(t):
        j = hash_actions.h(int(k[2:]), i)
        if t[j] is not None:
            if t[j][0] == k:
                return j
            else:
                i = i + 1
        else:
            i = i + 1
    return


def borrow_book(s, books, users):
    j = hash_actions.hash_insert(books, int(s[2][2:]))
    books[j] = [s[2], s[1], s[0]]
    h = hash_actions.hash_search(users, s[1])
    users[h].append(s[2])
    return books, users


def return_book(s, books, users):
    j = hash_search(books, s[2])
    books[j] = None
    h = hash_actions.hash_search(users, s[1])
    users[h].remove(s[2])
    # need to search inside user list for the book and remove it....
    return books, users


def find_book(s, books):
    j = hash_search(books, s[1])
    return books[j][1], books[j][2]
