import hash_actions


def add_user(s, users):
    # add user function receive the user command 's' and the arrays 'users' and adds the new user, complexity is O(1)
    j = hash_actions.hash_insert(users, int(s[2]))
    users[j] = [s[2], s[1]]
    return users


def remove_user(s, users):
    # remove user function receive the user command 's' and the arrays 'users' and removes the user, complexity is O(1)
    j = hash_actions.hash_search_users(users, s[2])
    users[j] = None
    return users


def find_user(s, users):
    # find user function for the '? USER_ID' query, receive user command 's' and users array and returns the user name
    # and id and list of books which they are currently borrowing, complexity is O(1)
    j = hash_actions.hash_search_users(users, s[1])
    return users[j][1], users[j][0], users[j][2:]


def books_check(s, users):
    # books check function checks weather or not the user already borrowing 10 books, complexity is O(1)
    j = hash_actions.hash_search_users(users, s[1])
    if len(users[j]) > 11:
        return True
    else:
        return False
