import mysql.connector,random
import login,randomcartid as cart
mydb=mysql.connector.connect(host="localhost",user="root",password="Mmakk2000$",database="electronic_appliance")
mycursor=mydb.cursor()
cart_id=cart.id


def payment(user_id,name,cart_id):
    e=input("Enter your email id: ")
    mycursor.execute("select carr_id as cart_id,sum(cost) as total_amount from addcart where carr_id={}".format(cart_id))
    d=mycursor.fetchone()
    print("Your overall purchase amount is: ",d[1])
    if(e==login.email_id):
        n7=int(input("-----Select payment method-----\n1. UPI\n2. Credit/debit/ATM card\n3. Cash on delivery"))
        if(n7==1):
            n8=int(input("Enter your UPI 4 digit Pin: "))
            n9=int(input("Enter your Total cost: "))
            if(n9==d[1]):
                print("Payment was Successfully completed!!!")
            else:
                n9=int("Enter your Total cost: ")
                if(n9==d[1]):
                    print("Payment was Successfully completed!!!")
        if(n7==2):
            n8=input("Enter your card number: ")
            n9=input("Expriy Date the format should be MM/YYYY: ")
            n10=int(input("Enter your 3 digit CVV number: "))
            c_otp=random.randint(1000,9999)
            print(c_otp)
            n11=int(input("Enter 4 digit otp: "))
            if(n11==c_otp):
                print("Payment was Successfully completed !!!")
            else:
                n10=n10=int(input("Enter your 3 digit CVV number: "))
                if(n11==c_otp):
                    print("Payment was Successfully completed !!!")
            if(n11==3):
                print("Your poduct will come by soon Thankyou !!!")
        if(n7==1 or n7==2):
            pay_status='successfull'
            if(d[0]>150000):
                reward=random.randint(100,999)
                print('Hyyy Buddy {} you own Rs.{}'.format(name,reward))
        else:
            pay_status='COD'
        print("Your cart id is {} future cancellation the products cart id it must so please note it your cart id.".format(cart_id))
        q='insert into payment(user_id,name,cart_id,pay_status,Total_amount) values(%s,%s,%s,%s,%s)'
        mycursor.execute(q,(user_id,name,cart_id,pay_status,d[1]))
        mydb.commit()
        

def addcart(p_id,p_name,p_price,qn,cost,a):
      
    q="insert into addcart (carr_id,user_id,name,p_id,p_name,p_price,quantity,cost)values (%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(q,(cart_id,login.user_id,login.name,p_id,p_name,p_price,qn,cost))
    mydb.commit()
    n6=int(input("If you want to continue purchase product ->enter 1 or payment means -> enter 2: "))
    if(n6==1):
        display()
    else:
        payment(login.user_id,login.name,cart_id)
      

    

def order(a):
    for i in a:
        n4=int(input("choose product id: "))
        if (n4==i[0]):
            pro_cost=i[4]
            pro_qn=int(input("Enter No of quantity:"))
            
            if (pro_qn<i[5]):
                mycursor.execute("update product_details set Avail_quality={} where p_id={}".format((i[5]-pro_qn),i[0]))
                mydb.commit()
                cost=pro_qn*pro_cost
    print("total cost: ",cost)
    addcart(i[0],i[3],i[4],pro_qn,cost,a)




def display():
    print("Welcome to e-shop!!!")
    mycursor.execute("select * from items")
    d=mycursor.fetchall()
    print("ID ITEMS\n--------------")
    print(d)
    for i in d:
        print(*i)
    print("--------------")
    n1=int(input("choose item id: "))
    mycursor.execute("select brand from product_Details where item_id={}".format(n1))
    b=mycursor.fetchall()
    print(*b)
    n2=input("choose brand: ")

    print("------------------------------------------")
    mycursor.execute("select * from product_details where item_id={} and brand={}".format(n1,n2))
    a=mycursor.fetchall()
    for i in a:
        print('product ID:',i[0],'\nProduct Name:',i[3],'\nProduct Price: ',i[4])
        print("\n---------------------------------------------------------------------------------------------\nProduct Description: ",i[6],'\n---------------------------------------------------------------------------------------')
    n3=int(input('if you want to order the product press 1 -> yes or press 0 ->no:'))
    if(n3==1):
        order(a)
    else:
        payment(login.user_id,login.name,cart_id)

display()
