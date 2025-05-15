import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="librarydb"
)

cursor = conn.cursor()


# Add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter year of publication: ")
    sql = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
    val = (title, author, year)
    cursor.execute(sql, val)
    conn.commit()
    print(f"\nBook '{title}' added successfully.\n")


# View all books
def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if books:
        print("\nBooks in Library:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
    else:
        print("\nNo books found.\n")


# Delete a book by ID
def delete_book():
    book_id = input("Enter book ID to delete: ")
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    print(f"\nBook with ID {book_id} deleted successfully.\n")


# Menu
def menu():
    while True:
        print("\n====== Library Book Management System ======")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Delete Book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


# Run the menu
if __name__ == "__main__":
    menu()

# Close connection when done
cursor.close()
conn.close()
