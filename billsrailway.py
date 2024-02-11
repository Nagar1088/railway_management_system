import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="S@16112001",
                             database="railway_management_system")
cursor=mydb.cursor()

while True:
    detail=input("Enter detail :")
    cost=input("Enter cost :")
    date=input("Enter  date(YY-MM-DD) : ")
    
    query="insert into bills(detail,cost,date) values(%s,%s,%s)"
    cursor.execute(query,(detail,cost,date))
    mydb.commit()

    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break
    