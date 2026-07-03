from db import conn,cursor 

def insert():

    name=input("Enter your name : ")
    sal=int(input("Enter your salary : "))
    query="insert into emp (name,sal) values (%s,%s)"
    values=(name,sal)
    cursor.execute(query,values)
    conn.commit()
    print("Data Inserted...")