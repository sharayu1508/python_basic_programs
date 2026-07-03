import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sharayu15",
    database="linkcode"
)
print("Database Connected ")

cursor=conn.cursor()
#create table 
cursor.execute( '''
   create table if not exists emp(
               empid integer primary key auto_increment,
               name varchar(20) not null ,
               sal decimal(10,2) check(sal>0)
               )

''')

conn.commit()
print("Table Created...")