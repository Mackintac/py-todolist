import tkinter as tkinter


# Initialize the root document of the application 
root = tkinter.Tk()

# Set the title of the application 
root.title("Mack's To-do List")



# Test code for python conditionals
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