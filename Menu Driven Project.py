#Code to implement various OS related tasks and etc.

import os               #OS Module is used to interact with the system OS
import webbrowser       #webbrowser Module is used to connect with the system's default web-browser.

print("Welcome.\n Depending upon your System Internet Access, \n you can perform various tasks.")

option='''
Press 1: To check internet access of your system.
Press 2: To run Task Manager.
Press 3: To run Calculator.
Press 4: To run MS Paint.
Press 5: To run MS Word.
Press 6: To make a Google search. (requires internet access)
Press 7: To make a Youtube search. (requires internet access) 
Press 8: To try the tasks again.
Press 9: To Exit the tasks.\n '''

def internet_access():
    result=os.system("ping -n 5 8.8.8.8")
    if(result==0):
        print("Internet is Working.")
    else:
        print("Internet is not working.\nCheck the internet connection and try again.")

def task_manager():
    result=os.system("%windir%\system32\Taskmgr.exe")
    if(result==0):
        print("Task Manager is Working.")
    else:
        print("Task Manager is not working.\nCheck your System32 Files and try again.")

def calculator():
    result=os.system("%windir%\system32\calc.exe")
    if(result==0):
        print("Calculator is Working.")
    else:
        print("Calculator is not working.\nCheck your System32 Files and try again.")

def ms_paint():
    result=os.system("%windir%\system32\mspaint.exe")
    if(result==0):
        print("MS Paint is Working.")
    else:
        print("MS Paint is not working.\nCheck your System32 Files and try again.")

def ms_word():
    result=os.system("%windir%\system32\write.exe")
    if(result==0):
        print("MS Word is Working.")
    else:
        print("MS Word is not working.\nCheck your System32 Files and try again.")

def google():
    print("Checking Google Access:\n")
    result=os.system("ping -n 5 www.google.com")
    if(result==0):
        print("Google is Working.\nEnter what you want to search:")
        search=input()
        search=search.replace(" ","+")
        url="https://www.google.com/search?q={}".format(search)
        webbrowser.open(url)
    else:
        print("Google is not working.\nCheck your network connection and try again.")

def youtube():
    print("Checking YouTube Access:\n")
    result=os.system("ping -n 5 www.youtube.com")
    if(result==0):
        print("YouTube is Working.\nEnter what you want to search:")
        search=input()
        search=search.replace(" ","+")
        url="https://www.youtube.com/results?search_query={}".format(search)
        webbrowser.open(url)
    else:
        print("YouTube is not working.\nCheck your network connection and try again.")

#Functions are defined for various tasks.
#driver's code
i=0
no_of_execution=0
while(i==0):
    print(option)
    choice=int(input("Enter your choice: "))
    if(choice==1):
        internet_access()
        no_of_execution+=1
    elif(choice==2):
        task_manager()
        no_of_execution+=1
    elif(choice==3):
        calculator()
        no_of_execution+=1
    elif(choice==4):
        ms_paint()
        no_of_execution+=1
    elif(choice==5):
        ms_word()
        no_of_execution+=1
    elif(choice==6):
        google()
        no_of_execution+=1
    elif(choice==7):
        youtube()
        no_of_execution+=1
    elif(choice==8):
        print("TRY AGAIN")
        no_of_execution+=1
    elif(choice==9):
        i+=1
        print("Total No. Of Execution:",no_of_execution)
        print("Developer Details:\nPUJA KUMARI\nGithub: https://github.com/puja-pearl\nThank You.")
    else:
        print("\nWrong Choice.\nTry Again.\n")
        no_of_execution+=1

#End Of Code

