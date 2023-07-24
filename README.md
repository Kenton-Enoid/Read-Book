# Book-Store

## This is a Python program that works with SQL Database specifically for a bookstore. The program should allow the clerk to enter data about new books into the database, update book information, delete books from the database and search to find the availability of books in the database.

## Table of Contents
1. **General Info**
2. **Tools**
3. **Installation**
4. **Usage**

## General Info
##### SQL is a standard language for storing, manipulating and retrieving data in databases. Using one of the most user-friendly language can make it easier for you to work around SQL data as it can store large amounts of data.

## Tools
1. Visual Studio Code (version 1.78.0)
2. Python (version 3.11.4)
3. SQLite Database

## Installation
1. Install VS Code (you can follow this link [https://www.python.org/downloads/release/python-3114/](https://code.visualstudio.com/download))
2. Install Python (you can follow this link https://www.python.org/downloads/release/python-3114/)
    * Add python packages by using "pip install" (visit Help section here: https://pypi.org/)
3. SQLite is a self-contained, serverless, zero-configuration, transactional SQL database engine that is part of the standard library of Python since version 2.51.
   This means that you can use SQLite in your Python programs without having to install any additional software or packages.
    * If you are using a virtual environment and want to use SQLite, you can simply import the sqlite3 module in your Python code. If you encounter any issues, you may need
    to ensure that the sqlite3.dll file is present in your virtual environment’s Scripts folder1. You can also try installing the pysqlite3 package using "pip install pysqlite3"
    within your virtual environment.
4. Connect the SQL database to the program by following these steps:
    * First we need to "import sqlite3 library into the program code.
    * Second, we need to create a new database and open a database connection to allow sqlite3 to work with it. Call sqlite3.connect() to create a connection to the database
      "ebookstore.db" in the current working directory, implicitly creating it if it does not exist:
    ![Alt text](https://github.com/Kenton-Enoid/Read-Book/blob/master/images/connection%20screenshot.png)

## Usage
### To use the program, follow these steps:
1. Open the .py file and run the program, you should be able to see the data as output and the options to select.
   ![Alt text](https://github.com/Kenton-Enoid/Read-Book/blob/master/images/Data%20%26%20Menu.png)
2. To enter data about new books into the database, select the “Enter New Book” option and follow the prompts:
   ![Alt text](https://github.com/Kenton-Enoid/Read-Book/blob/master/images/UsageAdd.png)
3. To update book information, select the “Update Book Information” option and follow the prompts.
4. To delete books from the database, select the “Delete Book” option and follow the prompts.
5. To search for books in the database, select the “Search for Books” option and enter your search criteria.
6. Enter 0 to exit program

## Get my GitHub repository below:
[myGitHubRepo](https://github.com/Kenton-Enoid/Read-Book)
    
