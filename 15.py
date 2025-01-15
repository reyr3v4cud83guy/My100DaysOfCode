class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, publication_year):
        self.books.append({
            "title": title,
            "author": author,
            "publication_year": publication_year
        })

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"{title} removed from the library.")
                return
        print(f"{title} not found in the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}, Publication Year: {book['publication_year']}")

    def display_total_books(self):
        print(f"Total number of books in the library: {len(self.books)}")

def main():
    library = Library()
    while True:
        print("\n1. Add book")
        print("2. Remove book")
        print("3. Display books")
        print("4. Display total books")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_year = input("Enter book publication year: ")
            library.add_book(title, author, publication_year)
        elif choice == "2":
            title = input("Enter book title: ")
            library.remove_book(title)
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            library.display_total_books()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()