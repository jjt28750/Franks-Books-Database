## Frank's Books Inventory and Sales Database System
## Jalen Tam
## System Analysis and Design Summer 2026 
##
## This code will be the first program that runs to create the database.  It will
## create the database, bookDatabase, as well as create the tables for entities.

## Imports
import mysql.connector


## Connect to MySQL server and log in.  Access database for Frank's Books: bookDatabase
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RootPassword22*",
    database="bookDatabase"
)

## Create variable for cursor in MySQL
mycursor = mydb.cursor()

## Create table for entity "book"
## bookID: Book ID, primary key
##  creating a unique bookID for each instance of book.
## title: Book title, cannot be empty
## price: Book price, cannot be empty
## inventoryCount: Number of books in inventory 
mycursor.execute("CREATE TABLE book (bookID INT(9) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, price INT(6) NOT NULL, inventoryCount INT(3))")

## Create table for entity "author"
## authorID: Author ID, primary key
##  creating a unique authorID for each instance of author
## authorFirstName: Author's first name, cannot be empty
## authorLastName: Author's last name, cannot be empty
mycursor.execute("CREATE TABLE author (authorID INT(9) AUTO_INCREMENT PRIMARY KEY, authorFirstName CHAR(25) NOT NULL, authorLastName CHAR(25) NOT NULL)")

## Create table for entity "genre"
## genreID: Genre ID, primary key
## genreName: Name of genre, cannot be empty
mycursor.execue("CREATE TABLE genre (genreID INT(9) AUTO_INCREMENT PRIMARY KEY, genreName CHAR(25) NOT NULL)")

## Create table for entity "supplier"
## supplierID: Supplier ID, primary key
## supplierName: Name of supplier, cannot be empty
## supplierEmail: Contact email for supplier, cannot be empty
## supplierPhoneNumber: Phone number for supplier, cannot be empty
## contactFirstName: First name of primary person of contact
## contactLastName: Last name of primary person of contact
mycursor.execute("CREATE TABLE supplier (supplierID INT(9) AUTO_INCREMENT PRIMARY KEY, supplierName CHAR(50) NOT NULL, supplierEmail VARCHAR(50) NOT NULL, supplierPhoneNumber INT(10) NOT NULL, contactFirstName CHAR(25), contactLastName CHAR(25))")

## Create table for entity "transaction"
## transactionID: Transaction ID, primary key
## time: Time of transaction, cannot be empty
## date: Date of transaction, cannot be empty
## totalPrice: Total price of transaction, cannot be empty
## paymentType: Payment time for transaction, cannot be empty
mycursor.execute("CREATE TABLE transaction (transactionID VARCHAR(9) PRIMARY KEY, time INT(5) NOT NULL, date INT(8) NOT NULL, totalPrice INT(7) NOT NULL, paymentType VARCHAR(20) NOT NULL)")