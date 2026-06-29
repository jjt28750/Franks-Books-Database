## Frank's Books Inventory and Sales Database System
## Jalen Tam
## System Analysis and Design Summer 2026 

## Imports
import mysql.connector

## Connect to MySQL server and log in.  Access database for Frank's Books: bookDatabase
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RootPassword22*",
    database="bookDatabase"
)

## Set variable for database cursor
mycursor = mydb.cursor()

mycursor