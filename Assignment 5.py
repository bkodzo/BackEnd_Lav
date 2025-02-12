def display_menu():
    print("\nChoose an option:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. View All Books")
    print("4. Exit")

def add_book(book_list):
    title = input("Enter the book title: ")
    book_list.append(title)
    print(f'"{title}" has been added to the library.')

def remove_book(book_list):
    if not book_list:
        print("The library is empty. No books to remove.")
        return
    
    title = input("Enter the book title to remove: ")
    if title in book_list:
        book_list.remove(title)
        print(f'"{title}" has been removed from the library.')
    else:
        print(f'"{title}" was not found in the library.')

def view_books(book_list):
    print("\nBooks in the Library:")
    if not book_list:
        print("No books in the library.")
    else:
        for book in book_list:
            print(f"- {book}")

def main():
    print("Welcome to the Book Title Library!")
    book_list = []
    
    while True:
        display_menu()
        
        # Check User Input 
        try:
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                add_book(book_list)
            elif choice == "2":
                remove_book(book_list)
            elif choice == "3":
                view_books(book_list)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception as e:
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()
