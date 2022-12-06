from maininvoice import invoice
from dataoutput import inventory

def update():
    b=invoice()#calling invoice
    file=open("data.txt",'w')#opening file to write
    for i in range(len(b)):#loop 
        a=b[i][0]+","+str(b[i][1])+","+str(b[i][2])#index
        file.write((str(a)))
        file.write('\n')
    file.close()
    
    return "INVENTORY IS UPDATED"
