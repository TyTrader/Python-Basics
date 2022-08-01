import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='carshowroom'
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE customer(Firstname VARCHAR(255), Lastname VARCHAR(255), Stateaddress VARCHAR(255), Cityaddress VARCHAR(255))')
mycursor.execute('INSERT INTO customers (Firstname, Lastname, Stateaddress, Cityaddress) VALUES (%s, %s, %s, %s)',
                 ('Carl', 'Johnson', 'Colorado', 'Denver'))

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
