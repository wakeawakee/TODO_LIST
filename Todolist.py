#TODOLIST
import json as j 

tasks=[]

    
def add_task(title,status):  #This func is used to add tasks
        task={'Title':title,'Status':status}
        tasks.append(task)
        file=open('task.json','w') #It open a file and writes all the task 
        j.dump(tasks,file)         #that user enter in file
       

        
    
def remove_task(index): #This func is used to remove task
        
             if index < len(tasks):
                removed_task = tasks.pop(index)

             else:
                print("Index out of range.")
                
          
        
def complete_task(index): #This func is used to make the status of task complete
             global tasks
             if index < len(tasks):
                  tasks[index]['Status']='Completed'
                  
             else:
                  print("Invalid Index")     
    
def Display_task(): #This func is used to display all the task you have added 
        for task in tasks:
            print(task)

def Load_Tasks():  #This func is used to load tasks from file to console
      file=open("task.json","r")
      data=j.load(file)
            
      print(data)

print("-------------------------------") 
print("1.Add Task->")
print("2.Remove Task-> ")
print("3.Mark Task as complete->")
print("4.Display Task->")
print("5.View_history")
print("6.Exit")
print("-------------------------------")
while True:
    
    choice=input("Enter the choice->")

    if choice=='1':
        title1=input("Enter the task->")
        add_task(title1,'Pending')

    elif choice=='2':
        index=input(("Enter task index to remove->"))
        remove_task(int(index))
    
    
    elif choice=='3':
        index=input(("Enter the task index to mark as complete->"))
        complete_task(int(index))

    elif choice=='4':
        Display_task()

    elif choice=='5':
        Load_Tasks() 
    elif choice=='6':
        break   

    else:
        print("Invalid")
        