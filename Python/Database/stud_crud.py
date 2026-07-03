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
cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(1,"ram","21"))
conn.commit()
print("Data Inserted...")


#User input
sid=int(input("Enter your id : "))
sname=input("Enter your name : ")
age=int(input("Enter your age : "))
cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(sid,sname,age))
conn.commit()

print("Data Inserted...")

#entire rows[()]

cursor.execute("select * from stud ")
rows=cursor.fetchall()
print(rows)
for r in rows:
    print(f"{r[0]}")

#single 

sid=int(input(("Enter the id : ")))
cursor.execute("select * from stud where sid=?",(sid,))
row=cursor.fetchone()
print(row)

#update
sid=int(input("Enter the id : "))
cursor.execute("select * from stud where sid=?",(sid,))
row=cursor.fetchone()
print(row)
if sid==row[0]:
    new_name=input("Enter new name : ")
    cursor.execute("update stud set name=? where sid=?",(new_name,sid))
    conn.commit()
    print("Updated Successfully...")
else:
    print("No record found!!!")

cursor.execute("select name,age from stud where age between 18 and 25 ")
rows=cursor.fetchall()
print(rows)
