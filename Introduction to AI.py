print("Hello,Iam an Al Chatbot.What is your name")
name=input()

print (f"Nice to meet you {name}.\n How may i assist you today?\n1. Apply for leave\n2.book appointment with the Nurse\n3.Exit")

choice=input()
if choice=='1':
    grade=input("enter your grade")
    reason=input("enter your reason:\n")
    print(f"Name:{name}\nGrade:{grade}\nReason for leave\n{reason} ") 
    print("Leave successfully Approved")
  
elif choice=='2':
    grade=input("enter your grade")
    reason=input("enter your reason:\n")
    print(f"Name :{name}\nGrade:{grade}\nReason for leave\n{reason} ") 
    print("Appointment Done")
    
elif choice=='3':
    print("Thank you for using our chatbot assistant")
    exit