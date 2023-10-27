# Ex2 - Array
# arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]

#1 - Sum all number (function)
def Sum(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    return sum
array = [10, 12, 3, 8, 9, 12, 12, 10, 10]
print(Sum(array))

#2 - Reverse array (function)
# def reverse(array):
#     newarr=[]
#     lastinde4x=len(array)-1
#     for i in range(len(array)):
#         newarr.append(array[lastinde4x-i])
#     return newarr
# arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# print(reverse(arr))

#3 - Find index of 3 (function)
# def PositionOf3(arr):
#     index=None
#     for i in range(len(arr)):
#         if arr[i]==3:
#             index=i
#     return index
# arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# print(PositionOf3(arr))

#4 - Romove 8 number from list (function)
# def PositionOf8(arr):
#     index=None
#     for i in range(len(arr)):
#         if arr[i]==8:
#             index=i
#     return index
# arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# n=PositionOf8(arr)
# arr.pop(n)
# print(arr)

#5 - Remove duplicate value (function)
# def check(Value,arr):
#     isSame=True
#     for i in range(len(arr)):
#         if Value==arr[i]:
#             isSame=False
#     return isSame
# arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# newarr=[]
# for i in range(len(arr)):
#     if check(arr[i],newarr):
#         newarr.append(arr[i])
# print(newarr)

#6 - Replace 10 by 99
# def replaceNumber(arr):
#     for i in range(len(arr)):
#         if arr[i]==10:
#             arr[i]=99
#     return arr
# arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
# print(replaceNumber(arr))
