import os

BOOK_FILE = "books.txt"

def load_books():
    if not os.path.exists(BOOK_FILE):
        return []
    with open(BOOK_FILE, "r") as f:
        books = []
        for line in f:
            if "|" in line:
                title, author, status = line.strip().split("|")
                books.append({"title": title, "author": author, "status": status})
        return books

def save_books(books):
    with open(BOOK_FILE, "w") as f:
        for b in books:
            f.write(f"{b['title']}|{b['author']}|{b['status']}\n")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    books = load_books()
    books.append({"title": title, "author": author, "status": "Available"})
    save_books(books)
    print("Book added.")

def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return
    print("\n--- BOOK LIST ---")
    for i, b in enumerate(books, 1):
        print(f"{i}. {b['title']} by {b['author']} - {b['status']}")
    print("------------------\n")

def borrow_book():
    books = load_books()
    if not books:
        print("No books available.")
        return
    view_books()
    try:
        choice = int(input("Enter book number to borrow: "))
    except:
        print("Invalid input.")
        return
    if 1 <= choice <= len(books):
        if books[choice-1]["status"] == "Available":
            books[choice-1]["status"] = "Borrowed"
            save_books(books)
            print("Book borrowed.")
        else:
            print("Already borrowed.")
    else:
        print("Invalid number.")

def return_book():
    books = load_books()
    if not books:
        print("No books available.")
        return
    view_books()
    try:
        choice = int(input("Enter book number to return: "))
    except:
        print("Invalid input.")
        return
    if 1 <= choice <= len(books):
        if books[choice-1]["status"] == "Borrowed":
            books[choice-1]["status"] = "Available"
            save_books(books)
            print("Book returned.")
        else:
            print("This book wasn't borrowed.")
    else:
        print("Invalid number.")

def search_book():
    books = load_books()
    if not books:
        print("No books available.")
        return
    name = input("Enter book name to search: ").lower()
    print("\n--- SEARCH RESULTS ---")
    found = False
    for b in books:
        if name in b["title"].lower():
            print(f"{b['title']} by {b['author']} - {b['status']}")
            found = True
    if not found:
        print("No matching book found.")
    print("------------------------\n")

def menu():
    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")
        print("==========================")
        choice = input("Choose (1-6): ")

        if choice == "1": add_book()
        elif choice == "2": view_books()
        elif choice == "3": borrow_book()
        elif choice == "4": return_book()
        elif choice == "5": search_book()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()
