def inventory():
    file = open("data.txt","r")
    l=[]
    lines = file.readlines()
    for line in lines:
        x=line.replace("\n","").split(',')
        l.append(x)
    file.close()
    for i in range(len(l)):
        l[i][0]=l[i][0].lower()
        l[i][1]=int(l[i][1])
        l[i][2]=int(l[i][2])
    return l

def display():
    print("The available products are")
    print ('Product \t price \t quantity')
    for each in inventory():
        if (len(each[0])<7):
            print (each[0],'\t\t',each[1],'\t',each[2])
        else:
            print (each[0],'\t',each[1],'\t',each[2])
    return ""

