import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="student"
)
mycursor = mydb.cursor()


def main_menu():
    ch = 'y'
    while ch == 'y':
        print("Student management System")
        print("1. Records management")
        print("2. Result management")
        choice = input("enter your choice:")

        if choice == '1':
            adrec()
        elif choice == '2':
            acdrec()
        else:
            print("wrong input.")

        ch = input("Do you want to continue?(y/n)")


def adrec():
    n = "y"
    while n == "y":
          print("Record management")
          print("1.To create a new table")
          print("2.To show existing tables")
          print("3.To describe structure")
          print("4.To add the record of a new student")
          print("5.To delete a record")
          print("6.To view record of a student")
          print("7.To alter a record")
          print("8.To view all records")
          print("9.To QUIT")
          ch = input("enter your choice:")
          if ch == '1':
              create_table()
          elif ch == '2':
              show_table()
          elif ch == '3':
              desc_table()
          elif ch == '4':
              newStudent()
          elif ch == '5':
              deleteSturec()
          elif ch == '6':
              viewrec()
          elif ch == '7':
              updateStudent()
          elif ch == '8':
             displayStudent()
          elif ch == '9':
             print("EXITING")
             n = input("Do you want to continue to main menu?(y/n)")
             if n == "y" or "Y":
                main_menu()
             if n == "n" or "N":
                 break
                 mydb.close()
    


def create_table():
    createTable = """CREATE TABLE IF NOT EXISTS student (
        SROLL_NO VARCHAR(5),
        SNAME VARCHAR(50),
        FNAME VARCHAR(50),
        MNAME VARCHAR(50),
        PHONE CHAR(10),
        ADDRESS VARCHAR(100),
        SCLASS VARCHAR(5),
        SSECTION VARCHAR(5),
        SADMISSION_NO VARCHAR(10) PRIMARY KEY)"""
    mycursor.execute(createTable)
    mycursor.execute("COMMIT")
    print("Table created Successfully")


def show_table():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
    if mycursor.execute == "" :
        print("Error")


def desc_table():
    mycursor.execute("DESCRIBE student")
    for x in mycursor:
        print(x)
    if mycursor.execute == "" :
        print("Error")    


def newStudent():
    sroll_no = input("ENTER ROLL_NO : ")
    sname = input("\n ENTER STUDENT'S NAME : ")
    fname = input(" ENTER FATHER'S NAME : ")
    mname = input(" ENTER MOTHER'S NAME : ")
    phone = input(" ENTER CONTACT NO. : ")
    address = input(" ENTER ADDRESS : ")
    sclass = input(" ENTER CLASS : ")
    ssection = input(" ENTER SECTION : ")
    sadmission_no = input(" ENTER ADMISSION_NO   :   ")

    sql = "INSERT INTO student (sroll_no,sname,fname,mname,phone,address,sclass,ssection,sadmission_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (sroll_no, sname, fname, mname, phone, address, sclass, ssection, sadmission_no)

    mycursor.execute(sql, values)
    mycursor.execute("COMMIT")

def deleteSturec():
     adm_no=input("enter the admission number of student.")
     sql="DELETE FROM student WHERE sadmission_no=%s"
     mycursor.execute(sql,(adm_no,))
     mycursor.execute("commit")
     print("record deleted")

def viewrec():
    adm_no = input("Enter the admission no. of student: ")
    sql = "SELECT * FROM STUDENT WHERE sadmission_no = %s"
    mycursor.execute(sql, (adm_no,))
    data = mycursor.fetchone()
    if data is not None:
        for x in data:
            print(x)
    else:
        print("No record")

            
	    


def displayStudent():
    mycursor.execute("SELECT * FROM student")
    data = mycursor.fetchall()
    for x in data:
        print(x)


def updateStudent():
    admission_no = input("ENTER ADMISSION NO :")

    sql = "SELECT * FROM student WHERE sadmission_no= %s"
    mycursor.execute(sql, (admission_no,))
    data = mycursor.fetchall()

    print("PRESS 1 FOR NAME")
    print("PRESS 2 FOR CLASS")
    print("PRESS 3 FOR ROLL NO")
    print("PRESS 4 FOR OTHER OPTIONS")
    choice = int(input("Enter Your Choice"))
    if choice == 1:
        name = input("ENTER NAME OF THE STUDENT  :")
        sql = "UPDATE student SET sname= %s WHERE sadmission_no =%s"
        mycursor.execute(sql, (name, admission_no))
        mycursor.execute("COMMIT")
        print("NAME UPDATED")
    elif choice == 2:
        std = input("ENTER CLASS OF THE STUDENT   :")
        sql = "UPDATE student SET sclass= %s WHERE sadmission_no=%s"
        mycursor.execute(sql, (std, admission_no))
        mycursor.execute("COMMIT")
        print("CLASS UPDATED")
    elif choice == 3:
      roll_no = int(input("ENTER ROLL NO OF THE STUDENT:"))
      sql="UPDATE	student	SET	sroll_no=	%s	WHERE sadmission_no = %s"
      mycursor.execute(sql,(roll_no,admission_no))
      mycursor.execute("COMMIT")
      print("ROLL NO UPDATED")
    elif choice==4:
      mycursor.execute("DESCRIBE STUDENT")
      for x in mycursor:
         print(x) 
      c=input("Enter the field to be changed")
      newinfo=input("Enter updated information.")
      sql="UPDATE	student SET %s=%s	WHERE sadmission_no = %s"      
      mycursor.execute(sql,(c,newinfo,admission_no))
      mycursor.execute("commit")
      print("RECORD UPDATED")
def acdrec():
    print("RESULT MANAGEMENT")
    print("1. To create table")
    print("2. Describe structure")
    print("3. To add student record")
    print("4. To delete student record")
    print("5. To view report card of a student.")
    print("6. To view overall report.")
    print("7. TO QUIT")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            create_r_table()
        elif choice == "2":
            desc_r_table()
        elif choice == "3":
            add_r_record()
        elif choice == "4":
            del_r_record()
        elif choice == "5":
            r_card_one_stu()
        elif choice == "6":
            r_card_all()
        elif choice == "7":
            print("EXITING")
            n = input("Do you want to continue to the main menu? (y/n): ")
            if n == "y" or "Y":
                main_menu()
            if n == "n" or "N":
                 break
                mydb.close()

def create_r_table():
    create_table = """CREATE TABLE IF NOT EXISTS MARKS(
        SADMISSION_NO VARCHAR(10) PRIMARY KEY,
        SNAME VARCHAR(20),
        HINDI INT,
        ENGLISH INT,
        MATH INT,
        SCIENCE INT,
        SOCIAL INT,
        COMPUTER INT,
        TOTAL INT,
        AVERAGE DECIMAL
    )"""
    mycursor.execute(create_table)
    mycursor.execute("COMMIT")
    print("Table created successfully.")

def desc_r_table():
    mycursor.execute("DESCRIBE MARKS")
    for x in mycursor:
        print(x)

def add_r_record():
    admission_no = input("ENTER ADMISSION NO OF THE STUDENT: ")
    name = input("ENTER NAME OF THE STUDENT")
    hindi = int(input("ENTER MARKS OF HINDI: "))
    english = int(input("ENTER MARKS OF ENGLISH: "))
    math = int(input("ENTER MARKS OF MATH: "))
    science = int(input("ENTER MARKS OF SCIENCE: "))
    social = int(input("ENTER MARKS OF SOCIAL: "))
    computer = int(input("ENTER MARKS OF COMPUTER: "))
    
    total = hindi + english + math + science + social + computer
    average = total / 6

    sql = "INSERT INTO MARKS(SADMISSION_NO,SNAME, HINDI, ENGLISH, MATH, SCIENCE, SOCIAL, COMPUTER, TOTAL, AVERAGE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (admission_no,name, hindi, english, math, science, social, computer, total, average)

    mycursor.execute(sql, values)
    mycursor.execute("COMMIT")
    print("\nMarks of the Student Entered Successfully!")

def del_r_record():
    adm_no = input("Enter the admission number: ")
    sql = "DELETE FROM MARKS WHERE SADMISSION_NO = %s"
    mycursor.execute(sql, (adm_no,))
    mycursor.execute("COMMIT")
    print("Record deleted successfully")

def r_card_all():
    mycursor.execute("SELECT * FROM MARKS")
    data = mycursor.fetchall()
    c = {}
    for x in data:
        c["AdmNo."] = x[0]
        c["Name:"] = x[1]
        c["Hindi:"] = x[2]
        c["English:"] = x[3]
        c["Maths:"] = x[4]
        c["Science:"] = x[5]
        c["S.ST"] = x[6]
        c["Computer"] = x[7]
        c["Total"] = x[8]
        c["Average"] = x[9]
        print(c)

def r_card_one_stu():
    admission_no = input("ENTER ADMISSION NO OF THE STUDENT: ")
    sql = "SELECT * FROM MARKS WHERE SADMISSION_NO = %s"
    mycursor.execute(sql, (admission_no,))
    data = mycursor.fetchall()
    if data is not None:
        for x in data:
            print(x)
    else:
        print("No record")
# Call the main menu function to start the program
main_menu()

