
from os import system, name
import getpass
import json

f = open("data.txt",'r')
x = json.load(f)
f.close()
b=open("database.txt",'r')
money=json.load(b)
b.close()



def check(a):

    if(len(a)<8):
        return False
    special = '[@_!#$%^&*()<>?/\|}{~:]'
    numbers='0123456789'
    boo = False
    booll=False
    for i in a:
        if(i in special):
            boo = True
        if (i in numbers):
            booll= True
    if boo == False or booll==False:
        return False
    

    return True

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def userMaker():
    root = True
    print("1)enter your full name: ")
    f=input()
    print("2)enter the password: ")
    u=getpass.getpass()
    while(check(u) == False):
        print("enter a strong password. use numbers and special characters")
        u=getpass.getpass()
    print("3)enter again for confirmation: ")
    g=getpass.getpass()
    if u==g:
        pass
    elif u!=g:
        print("password doesn't match. enter again")
        j=input()
        if u==j:
            pass
        else:
            print("you have entered the wrong password multiple times.")
            root=False
    if(root == False):
        return
    print("4)enter your initial amount: ")
    k=int(input())
            

    x[f]=u
    money[f]=k

def signIn():
    print("1)sign in")
    f=input("enter the username: ")
    i=getpass.getpass(prompt="enter the password: ")
    if f not in x:
        print("wrong username")
        return
    elif f in x and x[f]!=i:
        print("wrong password")
    elif i==x[f]:
        while(1):
            print("1)would u like to deposit")
            print("2)would u like to withdraw")
            print("3)delete the account")
            print("4)show details of the account")
            print("5)logout")
            p = int(input("enter the choice: "))
            if p==1:
                print("2)enter the amt: ")
                u=int(input())
                if u<=10000:
                    print("u can't be a member here")
                elif u>100000000:
                    print("we need to check your accounts to make this deposit due to legal reasons")
                    if money[f]>=10000000:
                        print(u+money[f])
                        money[f]=u+money[f]
                        print("thankyou")
                    else:
                        print("sorry.You are not legally allowed to make this transaction")
                else:
                    print(u+money[f])
                    money[f]=u+money[f]
                    print("thankyou")
            elif p==2:
                print("2)enter the amt: ")
                u=int(input())
                if money[f]-u < 0:
                    print("you don't have this amount of money in your account")
                    pass
                else:
                    print(money[f]-u)
                    money[f]=money[f]-u
            elif p==3:
                print("account deleted")
                del x[f]
                del money[f]
                return
            elif p==4:
                print(f'name: {f}')
                print(f'amount: {money[f]}')
            elif p==5:
                return
            else:
                print("this option doesn't exist")

def menu():
    print("WELCOME")
    print("what would u like to do today")
    print("1)make a new user: ")
    print("2)sign in: ")
    print("3)exit: ")

while(1):
    menu()
    y=int(input("enter the choice: "))
    if y==1:
        userMaker()
    elif y==2:
        signIn()
    elif y==3:
        print("come back soon")
        break
    else:
        print("this option doesn't exist")

print("Thanks for visiting.")

f=open("data.txt",'w')

json.dump(x,f)

f.close()
b=open("database.txt",'w')
json.dump(money,b)
b.close()




# take username and paswd
# menu()
# 3 transaction del show detail


