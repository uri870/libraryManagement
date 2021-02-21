def get_input():
    # get user input and split it into the list 's' and return
    s = [str(item) for item in input("\nPlease enter command : ").split()]
    return s


def print_found_books(user, id, books):
    # print results for the query '? USER_ID'
    print("The books found for the user: " + str(user) + " " + str(id) + " are: ", end="")
    for a in books:
        print(a, end=" ")
    print(" ")


def print_found_user(book, user):
    # print results for the query '? BOOK_ID'
    print("The user found for the book: " + str(book) + " is: " + str(user[0]) + " " + str(user[1]))


def print_user_added(user, id):
    # prints user added confirmation message
    print("The user: " + str(user) + " with id: " + id + " has been ADDED to the system.")


def print_user_removed(user, id):
    # prints user removed confirmation message
    print("The user: " + str(user) + " with id: " + id + " has been REMOVED from the system.")


def print_book_borrowed(book, id):
    # prints book borrowed confirmation message
    print("The book: " + str(book) + " has been BORROWED by user: " + id + ".")


def print_book_returned(book, id):
    # prints book returned confirmation message
    print("The book: " + str(book) + " has been RETURNED by user: " + id + ".")


def print_max_reached(s):
    # prints error message if user tries to borrow more than 10 books
    print("Can't borrow book! The user with id: " + s[1] + " already borrowed 10 books.")


def echo_cmd(s):
    # reflect back to user command typed
    print("\nCommand received: ", end=" ")
    for a in s:
        print(a, end=" ")
    print("\n")


def print_current_status(users, books):
    # diagnostic tool to view books and users arrays
    print("Current users: " + str(users))
    print("Current books: " + str(books))
    print("There are "+str(sum(value is None for value in users.values()))+" spaces left for users")
    print("There are " + str(sum(value is None for value in books.values())) + " spaces left for books")


def print_most_books(u):
    # print results for the query '? !'
    print("The users with the most books are: ")
    for a in u:
        print(a)
