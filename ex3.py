# Ex3 - Array 2D
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
#1 - How many number 2 in list

# def countNumber2(arr):
#     count=0
#     for i in range(len(arr)):
#         if arr[i]==2:
#             count+=1
#     return count
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# Count2=0
# for i in range(len(arr)):
#     Count2+=countNumber2(arr[i])
# print(Count2)

#2 - Sum only number > 5
# def sum(arr):
#     Sum=0
#     for i in range(len(arr)):
#         if arr[i]>5:
#             Sum+=arr[i]
#     return Sum
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# SumNumber=0
# for i in range(len(arr)):
#     SumNumber+=sum(arr[i])
# print(SumNumber)

#3 - How many number < 5
# def countNumber(arr):
#     count=0
#     for i in range(len(arr)):
#         if arr[i]<5:
#             count+=1
#     return count
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# Count=0
# for i in range(len(arr)):
#     Count+=countNumber(arr[i])
# print(Count)

#4 - Sum number in row
# def sum(n1,n2):
#     return n1+n2
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# Newarr=[]
# for i in range(len(arr)):
#     Sumall=0
#     for j in range(len(arr[i])):
#         Sumall=sum(Sumall,arr[i][j])
#     Newarr.append(Sumall)
# print(Newarr)

#5 - Sum number in column
# def sum(n1,n2):
#     return n1+n2
# arr = [
#   [1, 2, 3],
#   [2, 3, 4],
#   [5, 6, 8],
#   [10, 3, 8]
# ]
# Newarr=[]
# column=len(arr[0])
# row=len(arr)
# for i in range(column):
#     Sumall=0
#     for j in range(row):
#         Sumall=sum(Sumall,arr[j][i])
#     Newarr.append(Sumall)
# print(Newarr)

#6 - Replace number 8 with *
def change (array):
    for i in range(len(array)):
        if array[i]==8:
            array[i]="*"
    return array
arr = [
  [1, 2, 3],
  [2, 3, 4],
  [5, 6, 8],
  [10, 3, 8]
]
for i in range(len(arr)): 
    arr[i]=change(arr[i])
print(arr)