from time import strftime
from tkinter import Label, Tk

# Window config for clock
window = Tk()
window.title("Digital Clock")
window.geometry('200x100') # size of the window
window.configure(bg="black") # background color of window
window.resizable(False, False) # window showld be resizable or not
instance = Label(window,bg='blue',font=("Times",15,'bold'), relief='flat')
instance.place(x=55,y=35) 

def time():
    current_time=strftime("%H:%M:%S") # current time
    instance.config(text=current_time) # displying current time in tkinter window
    instance.after(80, time) # for updating time
time()    
window.mainloop()