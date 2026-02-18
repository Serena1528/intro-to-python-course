classesNum = int(input('Enter the number of classes you are taking: '))
class_names = ''
for i in range(classesNum):
    class_names += input('Enter the class name: \n')

print('Here are your classes: ')
print(class_names)