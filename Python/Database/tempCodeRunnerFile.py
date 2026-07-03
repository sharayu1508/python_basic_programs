import sqlite3

conn=sqlite3.connect("student.db")

cursor=conn.cursor()

#table crreation 

cursor.execute('''
        create table if not exists stud(
               sid integer primary key,
               name text not null,
               age integer null

               )
''')

print("Table Created!!!")

#insert
# cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(1,"ram","21"))
conn.commit()
print("Data Inserted...")


#User input
sid=int(input("Enter your id : "))
sname=input("Enter your name : ")