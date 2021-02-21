def find_most_books(users):
    # find most books function used to find the users with most books currently borrowed. the function is looping
    # through all users and books borrowed for each users and returns the name and id of all users with the maximum
    # amount of books, the complexity is the amount of users + maximum of 10 books each, which is in the worst case
    # O(n+10) = O(n)
    maximum = 0
    most_books_users = []
    u2 = users.items()

    for k in u2:
        # loop through all users
        for x in k[1:]:
            # loop through user's books (maximum 10 books)
            if x is not None:
                if len(x) > maximum:
                    # in case count of books > previous -> clear previous maximum value and add current, additionally
                    # add current user to the list of most books users
                    maximum = len(x)
                    most_books_users.clear()
                    most_books_users.append([k[1][0], k[1][1]])
                elif len(x) == maximum:
                    # in case count of books == previous -> add user to the list of most books users
                    most_books_users.append([k[1][0], k[1][1]])
    return most_books_users
