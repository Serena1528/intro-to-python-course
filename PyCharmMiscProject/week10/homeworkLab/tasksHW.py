#an empty list
todo_list = []
todo_completed = []

#asks the user for tasks and gives them the option to stop at any time
while True:
    #asks the user for the task name
    task = input('Enter your task, or press enter to stop: ')
    #if the user enters a null value the while loop stops and it prints all the information
    if not task:
        break
    #asks the user if the task is a completed one or not
    task_completed = input('Have you completed this task? (y/n: ')
    if task_completed.lower() == 'y':
        #if the task has been completed and is already in todo_completed then it doesnt add the task, and instead tells the user
        if task in todo_completed:
            print('You have already completed this task')
        #if the task has been completed and is not in todo_completed then it gets added to todo_completed
        else:
            todo_completed.append(task)
    elif task_completed.lower() == 'n':
        #checks if the task has already been added
        if task in todo_list:
            print('You have already added this task')
        #if the task is not in todo_list then it gets added to todo_list
        else:
            todo_list.append(task)
    #if the user enters a value that is not y or n then the loop ends and the information gets printed
    else:
        break

#makes sure that the lists have items in them to print out so there isn't weird formatting
if len(todo_list) > 0 or len(todo_completed) > 0:
    print('Thank you. Your tasks are')

#prints the tasks in todo_list and the number of it
for index, task in enumerate(todo_list):
    print(f'Uncompleted task {index+1} is {task}')

#prints the tasks in todo_completed and the number of it
for i, task in enumerate(todo_completed):
    print(f'Completed task {i+1} is {task}')

#gets the length of the lists and prints them
number_of_tasks = len(todo_list)
number_of_completed_tasks = len(todo_completed)
print(f'You have {number_of_tasks} tasks to do.')
print(f'You have {number_of_completed_tasks} completed tasks.')