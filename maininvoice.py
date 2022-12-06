import datetime
from random import randint
from dataoutput import inventory
def invoice():
    inven=inventory()
    print("FILLING BILL")
    name = str(randint(0,999999999))
    file=open(name+".txt",'w')    
    file.write("\t******************************************* UNIQUE ELECTRONIC STORE ********************************************\n")
    file.write("\tINVOICE BILL \n\t----------------------------------------------------------------------------------------------------------------\n")
    file.write("\tINVOICE Name : UEC")
    file.write(str(randint(1,500)))
    file.write('\t\t\t\t\tDATE AND TIME:  ')
    file.write(str(datetime.datetime.now()))
    file.write('\n')
    file.write(str("\tNAME: "))
    name=input('ENTER CUSTOMER NAME\t')
    file.write(str(name.upper()))
    file.write('\n')
    nextproduct="y"
    total=0
    file.write('\n')
    file.write(str("\tNAME OF PRODUCT\t"))
    file.write(str("\tBOUGHT QUANTITY\t"))
    file.write(str("\tAMOUNT per PRODUCT"))
    file.write(str('\tDISCOUNT AMOUNT\t'))
    file.write(str("\tFINAL PRICE"))
    file.write('\n')
    
    while nextproduct=="y":
        a=""
        price=0
        success = False
        while success == False:
            product=str(input('ENTER PRODUCT: '))
            x=0
            for x in range(len(inventory())):
                if product.lower()==inventory()[x][0]and (inventory()[x][2]!=0):
                    a=product.lower()
                    success =True
                    break
            if a=="":
                print("PRODUCT NOT AVAILABLE. RE ENTER THE PRODUCT: ")
                
        success2 = False
        while success2 == False:
            try:
                bought_quantity=int(input("ENTER BOUGHT QUANTITY: "))
                if bought_quantity>0 and (((inventory()[x][2])-bought_quantity)>=0):
                    success2 = True
                else:
                    print("INVALID VALUE FOR QUANTITY. ENTER VAID VALUE")
            except:
                print("INVALID VALUE FOR QUANTITY. ENTER VAID VALUE")
                
        inven[x][2]=inven[x][2]-bought_quantity#editing inventory
        
        success3 = False
        while success3 == False:
            try:
                discount=float(input("ENTER DISCOUNT PERCENTAGE"))
                if discount<100 and discount>=0:
                    succes3=True
                    break
                else:
                    print("enter less than 100 for discount or greater than or equal to zero")
                
            except:
                print("invalid value")
        
        for i in range(len(inventory())):
            if a==inventory()[i][0]:
                price=inventory()[i][1]

        file.write(str("\t")  )   
        file.write(a)

        file.write(str("\t\t\t")  )      
        file.write(str(bought_quantity))
                                   
        file.write(str("\t\t\t"))

        file.write(str(price))

        file.write(str("\t\t\t"))
        discountamount=(discount/100)*(price)
        file.write(str(discountamount))

        finalprice=(price*bought_quantity)-discount

        file.write(str("\t\t\t"))
        b=str(finalprice)
        file.write(b)
        file.write("\n")
        total=total+float(b)
        nextproduct=input("ENTER y FOR NEW PRODUCT")
        
    file.write('\n\n\n')
    file.write('\n')
    file.write('\t----------------------------------------------------------------------------------------------------------------')
    file.write('\n')
    file.write("\tTOTAL PRICE = ")
    file.write(str(total))
    file.write("\n\t****************************************************************************************************************")
    file.write("\n\tTHANK YOU FOR YOUR TIME HERE.\n\tHOPE TO SEE YOU AGAIN")
    file.write("\n\t****************************************************************************************************************")
    file.close()
    return inven
