import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'school'
)
mycursor = mydb.cursor()


#mycursor.execute('CREATE TABLE Primaryschools (National VARCHAR(255), Provincial VARCHAR(255), District VARCHAR(255), PrichoolID int PRIMARY KEY AUTOINCREMENT)')
#mycursor.execute('CREATE TABLE Secondaryschools (National VARCHAR(255), Provincial VARCHAR(255), District VARCHAR(255), SecschoolID int PRIMARY KEY AUTOINCREMENT)')
#mycursor.execute('CREATE TABLE University (Public VARCHAR(255), Private VARCHAR(255), Seminary VARCHAR(255), uniID int PRIMARY KEY AUTOINCREMENT)')

mycursor.execute('INSERT INTO PrimarySchools (National, Provincial, District)VALUES (%s, %s, %s)', ('Rockfields Junior', 'Bidii Primary', 'Bahati Primary'))
mycursor.execute('INSERT INTO Secondaryschools (National, Provincial, District)VALUES (%s, %s, %s)', ('Alliance high', 'Machakos Boys', 'Kiminini Boys'))
mycursor.execute('INSERT INTO University (Public, Private, Seminary)VALUES (%s, %s, %s)', ('UoN', 'Mount Kenya Uni', 'Scott Theological'))

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)