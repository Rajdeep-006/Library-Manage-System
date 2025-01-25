def display_books():
    """Displays the available books in the library."""
    print("\n========== Available Books ==========")
    for book, details in library.items():
        print(f"{book}: {details['copies']} copies available")
    print("====================================")

def borrow_book():
    """Allows a user to borrow a book from the library."""
    display_books()
    book_name = input("Enter the name of the book you want to borrow: ").strip()
    if book_name in library:
        if library[book_name]['copies'] > 0:
            library[book_name]['copies'] -= 1
            print(f"You have borrowed '{book_name}'. Please return it on time.")
        else:
            print(f"Sorry, '{book_name}' is currently not available.")
    else:
        print("The book is not available in the library.")

def return_book():
    """Allows a user to return a book to the library."""
    book_name = input("Enter the name of the book you want to return: ").strip()
    if book_name in library:
        library[book_name]['copies'] += 1
        print(f"Thank you for returning '{book_name}'.")
    else:
        print(f"'{book_name}' does not belong to this library.")

def add_book():
    """Allows an admin to add a new book to the library."""
    book_name = input("Enter the name of the book to add: ").strip()
    copies = input("Enter the number of copies to add: ").strip()
    if not copies.isdigit() or int(copies) <= 0:
        print("Invalid number of copies. Please enter a positive number.")
        return
    copies = int(copies)
    if book_name in library:
        library[book_name]['copies'] += copies
    else:
        library[book_name] = {'copies': copies}
    print(f"'{book_name}' has been added to the library with {copies} copies.")

def main():
    """Main function to run the library management system."""
    print("Welcome to the Library Management System!")
    while True:
        print("\n1. View Available Books\n2. Borrow a Book\n3. Return a Book\n4. Add a New Book\n5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            add_book()
        elif choice == '5':
            print("Thank you for using the Library Management System! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Sample library dictionary
library = {
    "The Great Gatsby": {"copies": 5},
    "1984": {"copies": 3},
    "To Kill a Mockingbird": {"copies": 4},
    "Pride and Prejudice": {"copies": 2},
    "Moby Dick": {"copies": 1}
}

if __name__ == "__main__":
    main()