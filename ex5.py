
# Ex5 - Array 2D
# arr = [
#   [0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 2]
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 1, 1]
# ]
#1 - How many 1 number in list
# def Count1(arr):
#     count=0
#     for i in range(len(arr)):
#         if arr[i]==1:
#             count+=1
#     return count
# arr = [
#   [0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 1, 1],
# ]
# Count=0
# for i in range(len(arr)):
#     Count+=Count1(arr[i])
# print(Count)

#2 - Replace 0 with $
# def change(arr):
#     for i in range(len(arr)):
#         if arr[i]==0:
#             arr[i]="$"
#     return arr
# arr = [
#   [0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 1, 1],
# ]
# for i in range(len(arr)):
#     arr[i]=change(arr[i])
# print(arr)

#3 - Replace 1 with 0 and replace 0 with 1
def change(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=1
        else:
            if arr[i]==1:
                arr[i]=0
    return arr
arr = [
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 1, 1],
]
for i in range(len(arr)):
    arr[i]=change(arr[i])
print(arr)