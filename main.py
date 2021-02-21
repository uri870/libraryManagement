""""
This Program is for library management which is used to manage library users and books.
**The program currently supports up to 100 users and books (the number can be increase by changing the 'm' variable
    in the main.py file).

The program provides the following operations:
1) Add user - adds new library user to the system, complexity in average is O(1)
2) Remove user - removes a library user from the system, complexity in average is O(1)
3) Borrow book - creates a new record of book borrowed by specific library user, complexity in average is O(1)
4) Return book - removes the record of a book borrowed by specific library user, complexity in average is O(1)
5) System queries:
    a) User query - finds all books borrowed by a specific user, complexity in average is O(1)
    b) Book query - finds the user currently borrowing a specific book, complexity in average is O(1)
    c) Most books query - Find the users currently borrowing the most books, complexity is O(n)

The program includes the following files:
main.py - implements the main program which allows user to input the desired command and execute the program functions.
user_management.py - handling user functions (adding, removing and user queries)
book_management.py - handling book functions (borrowing, returning and book queries)
most_books.py - implements the most books query
hash_actions.py - implements the hash table functions to store the data in the 'users' and 'books' hash tables
i_o.py - handles the inputs and outputs of the program

The program uses hash tables with open addressing algorithm to populate 2 arrays:
users: array of type dictionary holding a list for each user with the following fields: 'user name', 'id number' and
    'books borrowed'
books: array of type dictionary holding a list for each book with the following fields: 'book name', 'borrowing user
    id number' and 'borrowing user name'

The program uses hash tables and open addressing to store the data.
"""

import book_management
import most_books
import i_o
import user_management

m = 100  # hash tables size


def get_command():
    # Function to get user command input

    users = dict.fromkeys(range(m))  # Initializing users array
    books = dict.fromkeys(range(m))  # Initializing books array

    while 1:
        #  loop to continue receive user commands until exit
        user_input = i_o.get_input()  # s variable to hold user input
        if user_input[0] == "+":
            # add user operation
            i_o.echo_cmd(user_input)  # prints back command entered by the user
            users = user_management.add_user(user_input, users)  # add new user and assign to the user array
            i_o.print_user_added(user_input[1], user_input[2])  # prints user added message
            continue
        elif user_input[0] == "-":
            # remove user operation
            i_o.echo_cmd(user_input)  # prints back command entered by the user
            users = user_management.remove_user(user_input, users)  # remove user and assign to the user array
            i_o.print_user_removed(user_input[1], user_input[2]) # prints user removed message
            continue
        elif user_input[0] == "?":
            # queries operations
            i_o.echo_cmd(user_input)  # prints back command entered by the user
            if user_input[1][0].isdigit():
                # user query operation
                u, uid, b = user_management.find_user(user_input, users)  # returns user name, id and all books borrowed
                i_o.print_found_books(u, uid, b)  # prints query results
            elif user_input[1][0].isalpha():
                # book query operation
                i_o.print_found_user(user_input[1], book_management.find_book(user_input, books))  # prints query result
            else:
                # most books operation
                i_o.print_most_books(most_books.find_most_books(users))

            continue

        elif user_input[0] == "exit":
            # exit program in case user types 'exit'
            i_o.echo_cmd(user_input)
            print("goodbye!")
            exit(1)

        elif user_input[0] == "status":
            # diagnostic command to show data stored in arrays
            i_o.echo_cmd(user_input)
            i_o.print_current_status(users, books)

            continue

        elif user_input[3] == "+":
            # borrow book operation
            i_o.echo_cmd(user_input)  # prints back command entered by the user
            if not user_management.books_check(user_input, users):  # check if user already borrowed 10 books
                books, users = book_management.borrow_book(user_input, books, users)  # update users and books
                i_o.print_book_borrowed(user_input[2], user_input[1])  # print book added message
            else:
                i_o.print_max_reached(user_input)  # print error maximum books per user
            continue

        elif user_input[3] == "-":
            # Return book operation
            i_o.echo_cmd(user_input)  # prints back command entered by the user
            books, users = book_management.return_book(user_input, books, users)  # update users and books
            i_o.print_book_returned(user_input[2], user_input[1])  # print book returned message
            continue


if __name__ == '__main__':
    get_command()
