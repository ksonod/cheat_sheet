import tkinter as tk

def plus_1(x):
# add 1 to the input integer
    x=int(x)
    ret=x+1
    label = tk.Label(window, text="%d"%ret, font=("Arial", 16))
    label.place(x=10, y=70) # showing the current position


window = tk.Tk()
window.title("Sample window") # title
window.geometry("200x200") # size

############# Your Code #####

## Showing a text.
label = tk.Label(window, text="Type an integer", foreground="white", background="black", font=("Arial", 16))
label.place(x=10, y=10)

## Putting an entry box
#def_val = tk.StringVar()
entry = tk.Entry(window, width=10)
entry.place(x=10, y=40)

##
# if you click the button, one is added to the input integer.
button = tk.Button(window, text="Add 1", width=5, command= lambda : plus_1(entry.get()))
button.place(x=120,y=40) # change and update

############# Your Code #####

window.mainloop()
