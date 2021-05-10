import mysql.connector
import order,login,random,randomcartid as cart
mydb=mysql.connector.connect(host="localhost",user="root",password="Mmakk2000$",database="electronic_appliance")
mycursor=mydb.cursor()
cart_id=cart.id
s=[]
def p_cancel(p_id,qn,cost):
    s.append(cost)
    mycursor.execute("select Avail_quality from product_Details where p_id={}".format(p_id))
    n5=mycursor.fetchone()
    print(n5)
    n5=n5[0]
    mycursor.execute("update product_Details set Avail_quality={} where p_id={}".format(n5+qn,p_id))
    mydb.commit()
    mycursor.execute("delete from addcart where p_id={} and carr_id={}".format(p_id,cart_id))
    mydb.commit()
    

def cancel():
    n2=input("Enter your Email id: ")
    mycursor.execute("select * from user_details")
    res=mycursor.fetchall()

    for i in res:
        
        if(n2==i[3]):
            gen_otp=random.randint(1000,9999)
            print(gen_otp)
            n3=int(input("Enter your 4 digit otp: "))
            if(n3==gen_otp):
                print("Cart id: ",order.cart_id)
                mycursor.execute('select p_id,p_name,p_price,quantity,cost from addcart where carr_id ={}'.format(order.cart_id))
                n4=mycursor.fetchall()
                print("----------your products are---------")
                for i in n4:
                    print("Product id: ",i[0],'\nProduct name: ',i[1],'\nprice: ',i[2],'\nQuantity',i[3],'\ncost: ',i[4])
                    p_cancel(i[0],i[3],i[4])

    print("Your amount Rs.{} Refunded".format(sum(s)))    
                    
    
n1=int(input('If you want to cancel the order?\npress 1->yes\npress 2->no\n'))
if(n1==1):
    cancel()
