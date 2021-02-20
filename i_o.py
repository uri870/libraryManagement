def get_input():
    # set d function used to get user input for the variable 'd' and return it
    s = [str(item) for item in input("\nPlease enter command : ").split()]
    return s


def print_found_books(user, id, books):
    print("The books found for the user: " + str(user) + " " + str(id) + " are: ", end="")
    for a in books:
        print(a, end=" ")
    print(" ")


def print_found_user(book, user):
    print("The user found for the book: " + str(book) + " is: " + str(user[0]) + " " + str(user[1]))


def print_user_added(user, id):
    print("The user: " + str(user) + " with id: " + id + " has been ADDED to the system.")


def print_user_removed(user, id):
    print("The user: " + str(user) + " with id: " + id + " has been REMOVED from the system.")


def print_book_added(book, id):
    print("The book: " + str(book) + " has been BORROWED by user: " + id + ".")


def print_book_removed(book, id):
    print("The book: " + str(book) + " has been RETURNED by user: " + id + ".")


def print_max_reached(s):
    print("Can't borrow book! The user with id: " + s[1] + " already borrowed 10 books.")


def echo_cmd(s):
    print("\nCommand received: ", end=" ")
    for a in s:
        print(a, end=" ")
    print("\n")


def print_current_status(users, books):
    print("Current users: " + str(users))
    print("Current books: " + str(books))
    print("There are "+str(sum(value is None for value in users.values()))+" spaces left for users")
    print("There are " + str(sum(value is None for value in books.values())) + " spaces left for books")


def print_most_books(u):
    print("The users with the most books are: ")
    for a in u:
        print(a)
