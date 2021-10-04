import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="Lok@shgs22",database="music_class")

def admission():
    n=input("Enter student name -- ")
    a=input("Enter address -- ")
    p=input("Enter phone no -- ")
    a=input("Enter age -- ")
    f=input("Enter fees -- ")
    data=(n,a,p,a,f)
    sql='insert into admission values(%s,%s,%s,%s,%s)'
    cur=con.cursor()
    cur.execute(sql,data)
    con.commit()
    print(">-----------------------------------------------------<")
    print("Data entered successfully")
    main()

def Batch():
    s=input("Enter student name -- ")
    t=input("Enter teacher name -- ")
    st=input("Enter start time -- ")
    et=input("Enter end time -- ")
    d=input("Enter day -- ")
    data=(s,t,st,et,d)
    sql='insert into batch values(%s,%s,%s,%s,%s)'
    cur=con.cursor()
    cur.execute(sql,data)
    con.commit()
    print(">-----------------------------------------------------<")
    print("Data entered successfully")
    main()

def add_details():
    s='select * from admission'
    cur=con.cursor()
    cur.execute(s)
    myresult=cur.fetchall()
    for i in myresult:
        print("Student Name : ",i[0])
        print("Address",i[1])
        print("Phone no",i[2])
        print("Age",i[3])
        print("fees",i[4])
        print(">----------------------------------------------------<")
    main()

def batch_details():
    s='select * from batch'
    cur=con.cursor()
    cur.execute(s)
    myresult=cur.fetchall()
    for i in myresult:
        print("Student Name : ",i[0])
        print("teacher name",i[1])
        print("start time",i[2])
        print("end time",i[3])
        print("day",i[4])
        print(">----------------------------------------------------<")
    main()

def main():
    print("""
                                MUSIC CLASS ADMISSION
    1.Admission
    2.Batch
    3.Admission details
    4.Batch details
    5.Exit
    """)
    choice=input("Enter task no : ")
    print(">-------------------------------------------------------------<")
    if(choice=='1'):
        admission()
    elif(choice=='2'):
        Batch()
    elif(choice=='3'):
        add_details()
    elif(choice=='4'):
        batch_details()
    else:
        exit()

def run():
    main()
run()