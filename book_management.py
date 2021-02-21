import hash_actions


def borrow_book(s, books, users):
    # borrow book function receive the user command 's' and the arrays 'books' and 'users' and updates them with the
    # new book borrowed, complexity is O(1)
    j = hash_actions.hash_insert(books, int(s[2][2:]))  # calling 'hash insert' function to insert book, sending only
    # the 4 digit number part of the book id for open addressing algorithm
    books[j] = [s[2], s[1], s[0]]  # update 'books' array with the new book borrowed
    h = hash_actions.hash_search_users(users, s[1])  # find the user borrowing index
    users[h].append(s[2])  # update user record with the book borrowed
    return books, users


def return_book(s, books, users):
    # return book function receive the user command 's' and the arrays 'books' and 'users' and removes the book borrowed
    # complexity is O(1)
    j = hash_actions.hash_search_boooks(books, s[2])  # find book using hash search, sending only 4 digit part of book
    # id
    books[j] = None  # updates books array
    h = hash_actions.hash_search_users(users, s[1])  # find the user returning index
    users[h].remove(s[2])  # update user record, remove the book returned
    return books, users


def find_book(s, books):
    # find book function for the '? BOOK_ID' query, receive user command 's' and books array and returns the user name
    # and id which is currently holding the book, complexity is O(1)
    j = hash_actions.hash_search_books(books, s[1])
    return books[j][1], books[j][2]
