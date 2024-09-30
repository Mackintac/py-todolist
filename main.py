print("This line will be printed")

toDoListInit = {}
toDoListInit["Wake up at 7:00 AM EST"] = False
toDoListInit["Banana"] = False
toDoListInit["Exercise"] = False
toDoListInit["Think about very pretty amazing girlfriend"] = False
toDoListInit["Test Case"] = True

print(toDoListInit)


if input() == "Done":
    toDoListInit["Test Case"] = True
elif input() == "Pending":
    toDoListInit["Test Case"] = False
else:
    toDoListInit["Test Case"] = False


print(toDoListInit)