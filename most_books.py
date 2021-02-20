def find_most_books(users):
    maximum = 0
    maximum_users = []
    u2 = users.items()

    for k in u2:
        for x in k[1:]:
            if x is not None:
                if len(x) > maximum:
                    maximum = len(x)
                    maximum_users.clear()
                    maximum_users.append([k[1][0], k[1][1]])
                elif len(x) == maximum:
                    maximum_users.append([k[1][0], k[1][1]])
    return maximum_users
