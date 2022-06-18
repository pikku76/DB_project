import mysql.connector as c
con = c.connect(host="localhost", user="root", passwd="kali", database="astra")
cursor = con.cursor()
#if con.is_connected():
   # print("connected successfully...!!")

print("Bank Management System")

print("choose any one option for banking with us")
while True:
    choice = input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrawal\n4.Account Details\n5.ATM apply\n6.Exit")

     #1.open Account-->

    if choice == '1':

        name = input("enter your name::")
        age = int(input("enter your age::"))
        mob_number = int(input("enter your mob_number::"))

        #query for insert the values--->
        query = "insert into cst_detail values('{}',{},{})".format(name, age, mob_number)

        cursor.execute(query)
        con.commit()

        print("account open successfully")

        #Cash deposit-->

    elif choice == '2':
        name = input("enter your name::")
        amount = int(input("enter amount::"))

        query = "update cst_detail set amount = {} where name = '{}'".format(amount, name)

        cursor.execute(query)
        con.commit()
        print("cash deposit-->", amount)

        #Cash withdrawal

    elif choice == '3':
        name = input("enter your name::")
        amount = int(input("enter amount to withdraw::"))

        query = "update cst_detail set amount = {} where name = '{}'".format(amount, name)

        cursor.execute(query)
        con.commit()
        print("cash withdraw successful--->")

        #Account detail--->

    elif choice == '4':
        query = "select * from cst_detail"
        cursor.execute(query)
        acc_details = cursor.fetchall()
        print(acc_details)
        con.commit()

    elif choice == '5':
        name = input("enter your name::")
        age = int(input("enter your age::"))

        city = input("enter your city::")

        query = "insert into cst_detail values('{}',{},'{}')".format(name, age, city)

        cursor.execute(query)
        con.commit()
        print("you will get your ATM card soon")

    elif choice == '6':
        break
    else:
        print("invalid syntax")
