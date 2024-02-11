import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="S@16112001",
                             database="railway_management_system")
cursor=mydb.cursor()

while True:
    Name=input("Enter Name :")
    train=input("Enter train :")
    cost=int(input("Enter cost : "))
    distance=int(input("Enter distance :"))
    data=input("Enter data :")
    
    
    query="insert into customer(Name,train,cost,distance,data) values(%s,%s,%s,%s,%s)"
    cursor.execute(query,(Name,train,cost,distance,data))
    mydb.commit()

    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break