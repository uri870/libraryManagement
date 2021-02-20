import hash_actions


def add_user(s, users):
    j = hash_actions.hash_insert(users, int(s[2]))
    users[j] = [s[2], s[1]]
    print("The user was added to slot number "+str(j)+" in the array")
    return users


def remove_user(s, users):
    j = hash_actions.hash_search(users, s[2])
    users[j] = None
    return users


def find_user(s, users):
    j = hash_actions.hash_search(users, s[1])
    return users[j][1], users[j][0], users[j][2:]


def books_check(s, users):
    j = hash_actions.hash_search(users, s[1])
    if len(users[j]) > 11:
        return True
    else:
        return False
