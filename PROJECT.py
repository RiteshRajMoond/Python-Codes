names=['Anshul','Anudeep','Gurshan','Prateek','Ritesh','Sarthak','Sunil','Vansh','Vivek']
contact_No=['7906190034','9177421142','6280523905','7065810223','9463750884','9058558403','7056352798','7447047921','7340710317']
# global pin
pin=12216564

def all():
    for x in range(len(names)):
        print(names[x],":",contact_No[x])

def single():
    x=input("Enter Name: ",)
    y=x.capitalize()
    if y not in names:
        print("Not Found")
    else:
        z=names.index(y)
        print(names[z],":",contact_No[z])

def multiple():
    l=[]
    x=input("Enter Name: ",)
    y=x.capitalize()
    if y not in names:
        print("Not Found")
    else:
        z=names.index(y)
        l+=[z]
    while(True):
        print("Press '1' to enter another name \npress '2' to finish entering name")
        i=input("Enter your choice: ",)
        if(i=='1'):
            x=input("Enter Name: ",)
            y=x.capitalize()
            if y not in names:
                print("Not Found")
            else:
                z=names.index(y)
                l+=[z]
        elif(i=='2'):
            break
        else:
            print("Please enter from the given options")
    for x in l:
        print(names[x],":",contact_No[x])

def add():
    name=input("Enter name: ",)
    contact=int(input("Enter contact details: ",))
    pass1=int(input("Enter password: ",))
    if(pass1!=pin):
        print("Wrong Password")
        print("Process Stopped")
    else:
        print("Contact details added")
        names.append(name)
        contact_No.append(contact)

def edit():
    x=input("Enter the contact to be updated: ",)
    y=x.capitalize()
    if y not in names:
        print("Not found")
    else:
        print(y,"found in Database")
        pass1=int(input("Enter Password: ",))
        if(pass1!=pin):
            print("Wrong Password")
            print("Process Stopped")
        else:
            z=names.index(y)
            newnum=int(input("Enter updated numbber: ",))
            contact_No[z]=newnum
            print("Contact details added")

def delete():
    x=input("Enter Contact to be deleted: ",)
    y=x.capitalize()
    if y not in names:
        print("Not Found")
    else:
        print(y,"found in names")
        pass1=int(input("Enter Password: ",))
        if(pass1!=pin):
            print("Wrong Password")
            print("Process Stopped")
        else:
            z=names.index(y)
            names.remove(y)
            contact_No.remove(contact_No[z])
            print("Contact Deleted")
print('\n')
while(True):
    print("Press '1' to view all contacts \nPress '2' to select a single contact \nPress '3' to view multiple contacts \nPress '4' to add contact \nPress '5' to edit contact\nPress '6' to delete contact\nPress '9' to exit")
    press=input("Enter your choice: ")
    if(press=='1'):
        all()
    elif(press=='2'):
        single()
    elif(press=='3'):
        multiple()
    elif(press=='4'):
        add()
    elif(press=='5'):
        edit()
    elif(press=='6'):
        delete()
    elif(press=='9'):
        break
    else:
        print("Enter from the given options")
    print('\n')
