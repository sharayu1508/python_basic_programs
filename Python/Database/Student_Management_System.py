import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib
from email.message import EmailMessage

conn=sqlite3.connect("stud.db")

cursor=conn.cursor()

cursor.execute('''
    create table if not exists student(
               roll integer primary key,
               name text not null,
               java integer ,
               python integer,
               dbms integer,
               total integer,
               percentage float
               )
''')
print("Table Created Successfully...")




while True:
    print("*** MENU ***")
    print("\n1. Add records \n2. Update records \n3. Read records \n4. Search records \n5. Delete Records \n6. View result \n7. View reports \n8. Generate the pdf \n9. Exit")

    choice=int(input("Enter your choice : "))

    match choice:
        case 1:
            store=int(input(("How many students records do you want to store : ")))
            for i in range (0,store):
                print("Enter the Student Information : ")
                roll=int(input("Roll Number : "))
                name=input("Name : ")
                java=int(input("Java : "))
                python=int(input("Python :"))
                dbms=int(input("DBMS : "))

                cursor.execute("insert into student (roll,name,java,python,dbms) values(?,?,?,?,?)",(roll,name,java,python,dbms))
                conn.commit()
            print("Data Inserted Successfully...")

        case 2:
        
            print("\n1. Name \n2. Marks of java \n3. Marks of Python \n4. Marks of DBMS ")
            update=int(input("What do you want to update ? "))
            roll=int(input(("Enter Roll Number of that student : ")))
            if(update==1):
                cursor.execute("select * from student where roll=?",(roll,))
                row=cursor.fetchone()

                if row:
                    new_name=input("Enter new name : ")
                    cursor.execute("update student set name=? where roll=?",(new_name,roll))
                    conn.commit()
                    print(" Name Updated Successfully...")
                else:
                    print("No record found!!!")

            elif(update==2):
                cursor.execute("select * from student where roll=?",(roll,))
                row=cursor.fetchone()

                if row:
                    new_java=input("Enter new marks of java : ")
                    cursor.execute("update student set java=? where roll=?",(new_java,roll))
                    conn.commit()
                    print(" Java Marks Updated Successfully...")
                else:
                    print("No record found!!!")

            elif(update==3):
                cursor.execute("select * from student where roll=?",(roll,))
                row=cursor.fetchone()

                if row:
                    new_python=input("Enter new marks of python : ")
                    cursor.execute("update student set python=? where roll=?",(new_python,roll))
                    conn.commit()
                    print(" Python Marks Updated Successfully...")

                else:
                    print("No record found!!!")

            elif(update==4):
                cursor.execute("select * from student where roll=?",(roll,))
                row=cursor.fetchone()

                if row:
                    new_dbms=input("Enter new marks of DBMS : ")
                    cursor.execute("update student set dbms=? where roll=?",(new_dbms,roll))
                    conn.commit()
                    print(" DBMS Marks Updated Successfully...")

                else:
                    print("No record found!!!")
                    
            else:
                print("Record not found!!!")

        case 3:
            print("\n1.Read by roll Number \n2. Read all records ")
            ch=int(input("Enter your choice : "))

            if(ch==1):
                rn=int(input("Enter the Roll Number : "))
                cursor.execute("select * from student where roll=? ",(rn,))
                row=cursor.fetchone()
                print(row)

            elif(ch==2):
                cursor.execute("select * from student ")
                rows=cursor.fetchall()
                
                print("Roll\tName\t\tJava\tPython\tDBMS")
                print("-" * 50)

                for row in rows:
                    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}")

        case 4:
            print("Search the student record by ")
            print("\n1. Roll Number \n2. Name \n3.Marks")
            c=int(input("Enter your choice : "))
            if(c==1):
                r=int(input("Enter the Roll Number : "))
                cursor.execute("select * from student where roll=?",(r,))
                row=cursor.fetchone()
                print("Roll\tName\t\tJava\tPython\tDBMS")
                print("-" * 50)
                
                if row:
                 print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}")

            elif(c==2):
                    n=input("Enter the Name : ")
                    cursor.execute("select * from student where name=?",(n,))
                    row=cursor.fetchone()
                    print("Roll\tName\t\tJava\tPython\tDBMS")
                    print("-" * 50)
                        
                    if row:
                       print((f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}"))

            elif(c==3):
                t=int(input("Enter the Total marks : "))
                cursor.execute("select * from student where total=?",(t,))
                row=cursor.fetchone()  
                print("Roll\tName\t\tJava\tPython\tDBMS")
                print("-" * 50)              

                if row:
                    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}")

        case 5:
            print("\n1. Delete only on record \n2. Delete all records ")
            cho=int(input("Enter your choice : "))
            if(cho==1):
                roll_no=int(input("Enter the Roll Number of the student : "))
                cursor.execute("select * from student where roll=? ",(roll_no,))
                row=cursor.fetchone()
                if row:
                    cursor.execute("delete from student where roll=? ",(roll_no,))
                    conn.commit()
                    print("Record deleted successully!!!")
                else:
                    print("Record not found!!!")

            if(cho==2):
                cursor.execute("delete  from student ")
                conn.commit()
                print("All records deleted successfully...")

        case 6:
            cursor.execute("select * from student ")
            rows=cursor.fetchall()
            total=0
            for i in rows:
                total=0
                total=i[2]+i[3]+i[4]
                cursor.execute("update student set total=? where roll=? ",(total,i[0]))
                conn.commit()
                percentage=total/300*100
                cursor.execute("update student set percentage=? where roll=? ",(percentage,i[0]))
                conn.commit()
            
            cursor.execute("select * from student ")
            rows=cursor.fetchall()

            
            rol=int(input(("Enter your Roll Number : ")))
            cursor.execute("select * from student where roll=? ",(rol,))
            row=cursor.fetchone()
            print()
            print()
            print("*** Student Result ***")
            print("-" * 30 )            

            if row:
                print("Roll Number : ",row[0])
                print("Name of Student :",row[1])
                print("Java : ",row[2])
                print("Python : ",row[3])
                print("DBMS : ",row[4])
                print("-" * 30 )
                print("Total : ",row[5])
                print("Percentage : ",row[6])

        case 7:
            print("\n*** REPORTS ***")
            print("1. Pass Students")
            print("2. Fail Students")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                cursor.execute("""
                    SELECT * FROM student
                    WHERE java >= 35
                    AND python >= 35
                    AND dbms >= 35
                """)

                rows = cursor.fetchall()

                print("\n*** PASS STUDENTS ***")
                print("Roll\tName\tTotal\tPercentage")

                for row in rows:
                    print(f"{row[0]}\t{row[1]}\t{row[5]}\t{row[6]:.2f}")

            elif ch == 2: 
                cursor.execute("""
                    SELECT * FROM student
                    WHERE java < 35
                    OR python < 35
                    OR dbms < 35
                """)

                rows = cursor.fetchall()

                print("\n*** FAIL STUDENTS ***")
                print("Roll\tName\tTotal\tPercentage")

                for row in rows:
                    print(f"{row[0]}\t{row[1]}\t{row[5]}\t{row[6]:.2f}")
        
        case 8:
            rollno = int(input("Enter Roll Number : "))

            cursor.execute("select * from student where roll=?", (rollno,))
            row = cursor.fetchone()

            if row:

                roll = row[0]
                name = row[1]
                java = row[2]
                python = row[3]
                dbms = row[4]

                total = java + python + dbms
                percentage = (total / 300) * 100

                if java >= 35 and python >= 35 and dbms >= 35:
                    result = "PASS"
                else:
                    result = "FAIL"

                cursor.execute(
                    "update student set total=?, percentage=? where roll=?",
                    (total, percentage, roll)
                )
                conn.commit()

                # ---------------- Create PDF ----------------

                pdf = canvas.Canvas("Result.pdf")

                pdf.setFont("Helvetica-Bold",20)
                pdf.drawString(170,800,"STUDENT RESULT")

                pdf.setFont("Helvetica",14)

                pdf.drawString(70,760,"Name : "+name)
                pdf.drawString(70,735,"Roll No : "+str(roll))
                pdf.drawString(70,710,"java : "+str(java))
                pdf.drawString(70,685,"python : "+str(python))
                pdf.drawString(70,660,"dbms : "+str(dbms))
                pdf.drawString(70,635,"Total Marks : "+str(total))
                pdf.drawString(70,610,"Percentage : "+str(round(percentage,2))+" %")
                pdf.drawString(70,585,"Result : "+result)

                pdf.save()

                print("Result PDF Created Successfully.")

            receiver = input("Enter Email Address : ")

            sender = "sharayurjadhav@gmail.com"
            password = " axyn fzqr zjkn goax "

            msg = EmailMessage()

            msg["Subject"] = f"Student Result - Roll No. {roll}"
            msg["From"] = sender
            msg["To"] = receiver

            msg.set_content(f"""
            Dear {name},

            Your result has been generated successfully.

            Name : {name}
            Roll Number : {roll}

            Please find your result PDF attached with this email.

            Thank You.
            """)

            with open("Result.pdf", "rb") as f:
                file = f.read()

            msg.add_attachment(
                file,
                maintype="application",
                subtype="pdf",
                filename="Result.pdf"
            )

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

            server.login(sender, password)

            server.send_message(msg)

            server.quit()

            print("Result Sent Successfully!!")

        case 9 :
            print("Thank you for using the Student Management System.")
            conn.close()
            break
