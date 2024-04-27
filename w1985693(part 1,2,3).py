# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#student ID-W1985693
#Date-2023/04/19

def get_progression():               #to define a new function
    global total_credits                #to make the variable accessible from anywhere in the code
    global counts
    global Progress
    global Trailing
    global Retriever
    global Exclude
    global List
    global SubList
    while True:          #to run infinite time untill the break statement executes
     if total_credits != 120:
        break           #stop current logic and move onto the next logic
     if pass_credits == 120:
        p="Progress"
        print (p)
        Progress=Progress+1
        counts=counts+1
     elif pass_credits == 100:
        p="Progress (module trailer)"
        print (p)
        Trailing=Trailing+1
        counts=counts+1
     elif fail_credits==120 or fail_credits==100 or fail_credits==80:
        p="Exclude"
        print (p)
        Exclude=Exclude+1
        counts=counts+1
     else:
        p="Module retriever"
        print (p)
        Retriever=Retriever+1
        counts=counts+1
     SubList.append(p)
     SubList.append(pass_credits)
     SubList.append(defer_credits)
     SubList.append(fail_credits)
     List.append(SubList)       #to make a sublist inside the main list
     SubList=[]
     break

def display_histogram():
    global counts
    global Progress
    global Trailing
    global Retriever
    global Exclude
    print("-"*30)
    print("Histogram")
    print("Progress ",Progress ,": ","*"*Progress)
    print("Trailing ",Trailing ,": ","*"*Trailing)
    print("Retriever ",Retriever ,": ","*"*Retriever)
    print("Exclude ",Exclude ,": ","*"*Exclude)
    print(counts ,"outcomes in total")


def my_credit():
  while True:
    global total_credits
    total_credits=0
    global pass_credits
    global defer_credits
    global fail_credits
    
    try:         #to give user a hint about the error
        pass_credits = int(input("Enter number of credits at pass: "))
        pass_credits = int(pass_credits)
    except ValueError:   #to name the error  
        print("Integer required")
        break
    if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
        print("Out of range")
        break
    else:
        total_credits=total_credits+pass_credits
   

    
    
    try:
        defer_credits = int(input("Enter number of credits at defer: "))
        defer_credits = int(defer_credits)
    except ValueError:
        print("Integer required")
        break
    if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
        print("Out of range")
        break
    else:
        total_credits=total_credits+defer_credits
   

        
   
    try:
        fail_credits = int(input("Enter number of credits at fail: "))
        fail_credits = int(fail_credits)
    except ValueError:
        print("Integer required")
        break
    if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
        print("Out of range")
        break
    else:
        total_credits=total_credits+fail_credits

    if total_credits != 120:
        print ("Total incorrect")
    break

global counts
global Progress
global Trailing
global Retriever
global Exclude
counts=0
Progress=0
Trailing=0
Retriever=0
Exclude=0
global List
global SubList
List=[]
SubList=[]
my_credit()
get_progression()
print("Would you like to enter another set of data ?")
x=input("Enter 'y' for yes or 'q' to quit and view result : ")
x=x.lower()
while x=='y':
    my_credit()
    get_progression()
    print("Would you like to enter another set of data ?")
    x=input("Enter 'y' for yes or 'q' to quit and view result : ")
    x=x.lower()       #to make sure all the inputs are lowercase
f=open("List.txt","w")
L='\n'.join(str(e) for e in List)
f.write(L)
f.close
display_histogram()
print("Part 2 : ")
print(*List,sep="\n")
print("Part 3 : ")
f=open("List.txt","r")
print(f.read())
f.close()         # to close the file 


    


        
   

 
