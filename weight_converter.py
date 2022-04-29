from tkinter import *

#Size of the window (Height),(width)
HEIGHT = 220
WIDTH = 445

#Creating window
root = Tk()
root.title("Weighing machine")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.minsize(f"{WIDTH}",f"{HEIGHT}")
root.maxsize(f"{WIDTH}",f"{HEIGHT}")


#Taking User inputs
weight_of_user = Entry(root,font=("Consolas",16,"bold"),width=35)
weight_of_user.pack()

#converting Kg's into pounds 
def pounds_converter():
    try:
        if float(weight_of_user.get()) >= 1 and float(weight_of_user.get()) <=200 : 
            e_text=float(weight_of_user.get()) * 2.20462
            Label(root,text=e_text,font=("Consolas",16,"bold")).pack()
        else:
            wrong_parameter = "The input should  be > 1 and < than 200"
            labeling_errors = Label(root,text=wrong_parameter,font=("Consolas",12,"bold"))
            labeling_errors.pack()
    except:
        wrong_parameter = "The input should be an integer"
        labeling_errors = Label(root,text=wrong_parameter,font=("Consolas",12,"bold"))
        labeling_errors.pack()

#Creating buttons to show output on screen               
convert_btn = Button(root,text="Convert",command=pounds_converter,width=40,borderwidth=3)
convert_btn.pack()

root.mainloop()