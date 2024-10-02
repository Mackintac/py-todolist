from tkinter import *
from tkinter import ttk

# Initialize the root document of the application 
root = Tk()

# Set the title of the application 
root.title("Mack's To-do List")

# The main frame of which the content of the document is contained
content = ttk.Frame(root) 
frame = ttk.Frame(content, borderwidth=2, relief="ridge", width=5000, height=300)


nameLable = ttk.Label(content, text="Name")
name = ttk.Entry(content)


# Test code for python conditionals
toDoListInit = {}
toDoListInit["Wake up at 7:00 AM EST"] = False
toDoListInit["Banana"] = False
toDoListInit["Exercise"] = False
toDoListInit["Think about very pretty amazing girlfriend"] = False
toDoListInit["Test Case"] = True

todoOne = toDoListInit["Wake up at 7:00 AM EST"]

one = ttk.Checkbutton(content, text="One", variable= todoOne)

ok = ttk.Button(content, text="Enter")

cancel = ttk.Button(content, text="Cancel")


content.grid(column=0, row=0)

frame.grid(column=0, row=0, columnspan=3, rowspan=2)

nameLable.grid(column = 3, row = 0, columnspan = 2)

name.grid(column = 3, row = 1, columnspan = 2)

one.grid(column = 0, row = 3)

ok.grid(column = 3, row = 3)

cancel.grid(column = 3, row = 3)












print(toDoListInit)


if input() == "Done":
    toDoListInit["Test Case"] = True
elif input() == "Pending":
    toDoListInit["Test Case"] = False
else:
    toDoListInit["Test Case"] = False


print(toDoListInit)