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
# minute = (t - ((day * 86400) + (hour * 3600))) // 60
# seconds = t - ((day * 86400) + (hour * 3600) + (minute * 60))
# print(day, 'days', hour, ' hours', minute, 'minutes', seconds, ' seconds')

# ################################################################

# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum
#
# print(listsum([1,2,3,4]))

###############################################################
# list1 = [1,2,3,4]
# def summa_while(b):
#     index = 0
#     element = 0
#     while index < len(b):
#         element += b[index]
#         index += 1
#         return element
#
# task3_2 = summa_while(list1)
# print(task3_2)
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

# def fibo(n):
#     if n > 2:
#         return fibo(n-1) + fibo(n-2)
#     else:
#         return 1
# fbo = fibo(8)
# print(fbo)

##############################################
# def tomato(func):
#     def warapper():
#         print("помидор")
#         func()
#     return warapper
# def meat(func):
#     def warapper():
#         print("мясо")
#         func()
#     return warapper
#
# def cheese(func):
#     def warapper():
#         print("сыр")
#         func()
#     return warapper
#
# def bread(func):
#     def warapper():
#         print("хлеб")
#         func()
#     return warapper
# def food():
#  print()
#
# @tomato
# def food():
#     return None
# food()
# @meat
# def food():
#     return None
# food()
# @cheese
# def food():
#     return None
# food()
# @bread
# def food():
#     return None
# food()