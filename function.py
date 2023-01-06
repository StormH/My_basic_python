#
# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#     s = 0
#     for i in range(start, end + 1):
#         s += i
#     return s
#
# a, b = map(int, input().split())
# print(sum_range(a, b))
################################################################
# x = input('enter a positive integer: ')
#
# t = int(x)
#
# day = t // 86400
# hour = (t - (day * 86400)) // 3600
# minit = (t - ((day * 86400) + (hour * 3600))) // 60
# seconds = t - ((day * 86400) + (hour * 3600) + (minit * 60))
# print(day, 'days', hour, ' hours', minit, 'minutes', seconds, ' seconds')

# ################################################################

# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum
#
# print(listsum([1,2,3,4]))

###############################################################
list1 = [1,2,3,4]
def summa_while(b):
    index = 0
    element = 0
    while index < len(b):
        element += b[index]
        index += 1
        return element

task3_2 = summa_while(list1)
print(task3_2)
##############################################################

# list2 = [1,2,3,4,5]
# def summa(number,index=0):
#      if index >= len(number):
#          return 0
#      else:
#          return \
#         number[index]+summa(number,index+1)
# task3_3 = summa(list2)
# print(task3_3)

#############################################

# def fibonachi(n):
#     if n > 2:
#         return fibonachi(n-1) + fibonachi(n-2)
#     else:
#         return 1
# fboo = fibonachi(8)
# print(fboo)

##############################################
def tomato(func):
    def wrapper():
        print("помидор")
        func()
        return wrapper

def meat(func):
    def wrapper():
        print("мясо")
        func()
        return wrapper

def cheese(func):
    def wrapper():
        print("сыр")
        func()
        return wrapper

def bread(func):
    def wrapper():
        print("хлеб")
        func()
        return wrapper
def food():

 print()
sandwich = bread(ingredients(sendiwich))
sandwich()
@tomato
@meat
@cheese
@bread
def food():
 food()