import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="S@16112001",
                             database="railway_management_system")
cursor=mydb.cursor()

while True:
    name=input("Enter name :")
    train=input("Enter train :")
    train_number=int(input("Enter train_number : "))
    payment=int(input("Enter payment :"))
    data=input("Enter data :")
    phone_number=int(input("Enter phone_number :"))
    
    query="insert into customer(name,train,train_number,payment,data,phone_number) values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(name,train,train_number,payment,data,phone_number))
    mydb.commit()

    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break