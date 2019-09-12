import mysql.connector
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Zalkeandsons",
        database = "employee",
)
mycursor = mydb.cursor()
print("Menubar\n1. Insert\n2. Fetch Data\n3. Delete Data With Ref To id\n4. Break")
while True:
    c = int(input("Enter a choice: "))
    if c == 1:
        eid = int(input("Enter employee id: "))
        ename = input("Enter employye name: ")
        esalary = int(input("Enter empliyee's salary: "))
        ejd = (input("Employee joining date:(yyyy-mm-dd) "))
        sql1 = ("insert in info (eid, ename, esalary, ejd) values (%s, %s, %s, %s)")
        val = (eid, ename, esalary, ejd)
        mycursur.execute(sql1, val)
        mydb.commit()
        print(mycursur.rowcount(), "INserted")
        
    elif c == 2:
        mycursur.execute("select * from info")
        r = mycursur.fetchall()
        for i in r:
            print(i)
            
    elif c == 3:
        eid = int(input("Entr employee id to delete his/her data: "))
        mycursur.execute("delete from info where eid = %s" %eid)
        
    else:
        break
    
    