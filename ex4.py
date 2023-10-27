# Ex4 Array 2D
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
#1 - How many fruit in list
# def countFruit(arr):
#     return (len(arr))
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# count=0
# for i in range (len(arr)):
#     count+=countFruit(arr[i])
# print(count)

#2 - How many mango, orange, banana, coconut
# def countFruit(arr):
#     count=0
#     for i in range(len(arr)):
#         if arr[i].upper()=="MANGO":
#             count+=1
#     return count
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# countMango=0
# for i in range(len(arr)):
#     countMango+=countFruit(arr[i])
# print("Mango has : " + str(countMango))

# Orange?
# def countFruit(fruit,name):
#     count=0
#     for i in range(len(fruit)):
#         if fruit[i].upper()==name.upper():
#             count+=1
#     return count
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# Count=0
# for i in range(len(arr)):
#     Count+=countFruit(arr[i],"orange")
# print(Count)

# Banana
# def countFruit(fruit,name):
#     count=0
#     for i in range(len(fruit)):
#         if fruit[i].upper()==name.upper():
#             count+=1
#     return count
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# Count=0
# for i in range(len(arr)):
#     Count+=countFruit(arr[i],"banana")
# print(Count)

# coconut
# def countFruit(fruit,name):
#     count=0
#     for i in range(len(fruit)):
#         if fruit[i].upper()==name.upper():
#             count+=1
#     return count
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# Count=0
# for i in range(len(arr)):
#     Count+=countFruit(arr[i],"coconut")
# print(Count)

#3 - How many letter "o" in list
# def countLetterO(arr):
#     count=0
#     for i in range(len(arr)):
#         if arr[i].upper()=="O":
#             count+=1
#     return count
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
# CountO=0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         CountO+=countLetterO(arr[i][j])
# print(CountO)

#4 - How many fruits has 6 character
def CountCharcter(fruit):
    count=0
    if len(fruit)==6:
        count+=1
    return count
arr = [
  ['banana', 'mango', 'mango', 'Jackfruit'],
  ['orange', 'coconut', 'banana', 'papaya'],
  ['apple', 'orange', 'mango', 'coconut'],
  ['mango', 'coconut', 'banana', 'papaya'],
  ['banana', 'apple', 'orange', 'coconut'],
]
Count6=0
for i in range (len(arr)):
    for j in range(len(arr[i])):
        Count6+=CountCharcter(arr[i][j])
print(Count6)

