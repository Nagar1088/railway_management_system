import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="S@16112001",
                             database="railway_management_system")
cursor=mydb.cursor()

while True:
    name=input("Enter name :")
    salary=int(input("Enter salary"))
    Work=input("Enter Work : ")
    
    
    
    query="insert into customer(name,salary,Work) values(%s,%s,%s)"
    cursor.execute(query,(name,salary,Work))
    mydb.commit()

    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break