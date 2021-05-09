import mysql.connector,random,re

mydb=mysql.connector.connect(host="localhost",user="root",password="Mmakk2000$",database="electronic_appliance")
mycursor=mydb.cursor()


class Authentication():
    def __init__(self,username=''):
        self.username=username
    def validate(self):
        return re.match(r'[\w-]{1,20}@\w{1,20}\.\w{1,20}$',self.username)


def register():
    admin_user=input("if you are customer type -> user or admin means type->admin: ")
    name=input("Enter your name: ")
    email_id=input("Enter your email id: ")
    a=Authentication(email_id)
    valid=a.validate()
    if valid:
        pw=input("Create your password: ")
        pw1=input("Confirm your password: ")
        ph_no=input("Enter your phone number: ")
        address=input("Enter your Address: ")
        if(pw==pw1):
            gen1=random.randint(1000,9999)
            print(gen1)
            otp1=int(input("Enter your 4 digit pin: "))
            if(gen1==otp1):
                print("Successfully Registered!!!")
            else:
                print("Please Enter correct pin")
        query="insert into user_details (admin_or_user,name,email_id,password,ph_no,address)values(%s,%s,%s,%s,%s,%s)"
        val=[(admin_user,name,email_id,pw1,ph_no,address)]
        mycursor.executemany(query,val)
        mydb.commit()
    else:
        print("Enter valid email to register")
        register()
def check(c):
    if(c==0):    
        n=int(input("Invalid email id if you have an account press ->1 \nif you don't have an account press -> 2: "))
        if(n==1):
            mail()
        else:
            register()

def mod():
    user_id=i[0]
    name=i[2]
    email_id=i[3]


         
def mail():
    global email_id,user_id,name,c
    email_id=input("Enter your mail id: ")
    password=input("Enter your password: ")
    mycursor.execute("select * from user_details")
    res=mycursor.fetchall()
    c=0
    for i in res:
        if(i[3]==email_id and i[4]==password):
            c=1
            mod(res)
            
            break
    else:
        check(c)      
mail()

