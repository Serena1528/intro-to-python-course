#an empty list
todo_list = []

#asks the user for tasks and gives them the option to stop at any time
while True:
    task = input('Enter your task, or press enter to stop: ')
    if task:

        #checks if the task has already been added
        if task in todo_list:
            print('You have already added this task')
        else:
            todo_list.append(task)
    else:
        break

#prints the tasks in todo_list and the index that it is in
print('Thank you. Your tasks are')
for index, task in enumerate(todo_list):
    print(f'Task {index+1} is {task}')

#gets the length of the list and prints it
number_of_tasks = len(todo_list)
print(f'You have {number_of_tasks} tasks to do.')