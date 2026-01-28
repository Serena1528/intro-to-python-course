import random
from contextlib import nullcontext

num1 = random.randint(1,10)
num2 = random.randint(1,10)
num3 = random.randint(1,10)
num4 = random.randint(1,10)
num5 = random.randint(1,10)

nums = [num1, num2, num3, num4, num5]
numlength = len(nums)
finished = True
current = 0
temp = 0

print(nums)
#if num1 is greater than num2, then we want to make a temp variable to swap the two numbers, so tempA should
#get the value of num1, then num1 gets the value of num2, then num2 gets the value of tempA
while finished == True:
    if nums[current] > nums[current+1]:
        tempA = nums[current]
        nums[current] = nums[current+1]
        nums[current+1] = tempA
        print(nums)
    elif nums[current] < nums[current+1]:
        curent =+ 1
        if current == 5:
            finished = False
            print (nums)




