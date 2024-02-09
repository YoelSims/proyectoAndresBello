import mysql.connector

baseconexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "andresbello",
)

cursor = baseconexion.cursor()

cursor.execute("SHOW DATABASES")

for bd in cursor:  #Muestra las Bases de 
    print(bd)

