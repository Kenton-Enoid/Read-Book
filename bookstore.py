import sqlite3

# Define a function to create a database and table and insert initial data
def connection():
    # Connect to the ebookstore.db SQLite database
    db = sqlite3.connect('ebookstore.db')
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute a CREATE TABLE statement to create the books table if it doesn't already exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')
    
    # Check if the books table is empty
    cursor.execute('''SELECT COUNT(*) FROM books''')
    count = cursor.fetchone()[0]
    if count == 0:
        # If the books table is empty, insert the initial data into the table
        books = [(3001, "A Tale of Two Cities", "Charles Dickens", 30),
                 (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
                 (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
                 (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
                 (3005, "Alice in Wonderland", "Lewis Carroll", 12)]
        
        for book in books:
            cursor.execute('''INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', book)
    
    # Commit the changes to the database and close the connection
    db.commit()
    db.close()


# Define a function to insert a new book into the books table
# Connect to the ebookstore.db SQLite database
# Create a cursor object
# Execute an INSERT statement to insert a new row into the books table with the specified values
# Commit the changes to the database and close the connection
def enter_book(id, Title, Author, Qty):
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', (id, Title, Author, Qty))
    db.commit()
    db.close()

# Define a function to update an existing book in the books table
# Connect to the ebookstore.db SQLite database
# Create a cursor object
# Execute an UPDATE statement to update the row in the books table with the specified id with the new values
# Commit the changes to the database and close the connection
def update_book(id, Title, Author, Qty):
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()
    cursor.execute('''UPDATE books SET Title=?, Author=?, Qty=? WHERE id=?''', (Title, Author, Qty, id))
    db.commit()
    db.close()

# Define a function to delete an existing book from the books table
# Connect to the ebookstore.db SQLite database
# Create a cursor object
# Execute a DELETE statement to delete the row from the books table with the specified id
# Commit the changes to the database and close the connection
def delete_book(id):
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM books WHERE id=?''', (id,))
    db.commit()
    db.close()        

# Define a function to search for books in the books table by title and author
# Connect to the ebookstore.db SQLite database and create a cursor object
# Execute a SELECT statement to search for rows in the books table that match the specified
# title and author
def search_book(Title="", Author=""):  
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM books
                      WHERE Title=? OR Author=?''', (Title, Author))
    rows = cursor.fetchall()
    db.close()
    return rows

# Define a function that displays all books in store 
# This function connects to the ebookstore.db SQLite database, creates a cursor object,
# and executes a SELECT statement to retrieve all rows from the books table. It then fetches
# all rows returned by the SELECT statement, loops through each row, and prints it out.
# Finally, it closes the database connection.
def display_books():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM books''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    db.close()

# Define a function to display a menu of options to the user
def menu():
    display_books()

    print("ebook store menu below:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search book")
    print("0. Exit")

# Define the main function of the program
# Then call the connection function to create the database and table and insert initial data
def main():
    connection()
    
    # Enter an infinite loop to display the menu and prompt the user for input
    while True:
        menu()
        choice = input("Enter your choice: ")
        # Check if the user entered "1" to enter a new book
        # Prompt the user to enter the title, author and quantity of the new book
        if choice == "1":
            id = int(input("Enter book id: "))     
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            qty = int(input("Enter quantity: "))
    
            # Call the enter_book function with these values as arguments to insert a new row into the 
            # books table
            enter_book(id, title, author, qty)
            # Print a message to let the user know that the book was added successfully
            print("Book added successfully!")

        # Check if the user entered "2" to update an existing book
        # Prompt the user to enter the id of the book to update and its new title, author and quantity
        elif choice == "2":
            id = int(input("Enter book id: "))
            title = input("Enter new book title: ")
            author = input("Enter new book author: ")
            qty = int(input("Enter new quantity: "))
    
            # Call the update_book function with these values as arguments to update the corresponding row
            # in the books table
            update_book(id, title, author, qty)
            # Print a message to let the user know that the book was updated successfully
            print("Book updated successfully!")

        # Check if the user entered "3" to delete an existing book
        # Prompt the user to enter the id of the book to delete
        elif choice == "3":          
            id = int(input("Enter book id: "))
    
            # Call the delete_book function with this value as an argument to delete the corresponding row from 
            # the books table
            delete_book(id)
            # Print a message to let the user know that the book was deleted.
            print("Book deleted!")

        # Check if the user entered "4" to search for books
        # Prompt the user to enter a title or author to search for
        elif choice == "4":          
            title = input("Enter book title: ")
            author = input("Enter book author: ")
    
            # Call the search_book function with these values as arguments and store the matching rows in
            # a variable
            # Iterate over the matching rows and print each one
            books = search_book(title, author)
            for book in books:
                print(book)

        # Check if the user entered "0" to exit the program
        elif choice == "0":
            # Break out of the while loop to terminate the program
            break
        # If none of the above conditions are met, print an error message and prompt the user for input again
        else:
            print("Invalid choice. Please try again.")

# Check if this script is being run as the main program
if __name__ == "__main__":
    # If it is, call the main function to start the program
    main()

# Reference:
# https://learnsql.com/blog/sql-insert-sql-update-sql-delete-oh-my/