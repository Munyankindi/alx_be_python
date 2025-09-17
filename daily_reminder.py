task_variable = input("Enter task Description: ")
priority = input("Enter task Priority: high,Medium,Low: ")
time_bound = input("is the task time bound ? yes/no: ")
match priority:
    case "Low":
        print(task_variable,"is low priority task. cosider completing it when you have free time")
    case "Medium":
        print(task_variable ,"is medium priority that needs to be completed shortly after")
    case "high":
        if time_bound == "yes":
             print(task_variable,"is high priority task that requires immediate attention today!")
        else:
            print(task_variable,"is not time bound,you can do it later")
         

        
    

