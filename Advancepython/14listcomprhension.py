myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)


def new_func():
    list1 = [1, 7, 12, 11, 22]  # Ensure no extra comma
    list2 = [item for item in list1 if item > 8]  # Fix list comprehension

    print(list2)

new_func()