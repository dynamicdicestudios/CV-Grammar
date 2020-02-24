from tkinter import *
from grammar import main

def get_image():
    root = Tk()
    root.title("CV Grammar")
    root.geometry("300x180+500+250")

    Label(root, text="Enter the file location", font=("time new roman",10)).place(x=20,y=50)
    
    file=Entry(root)

    def fix_grammar():
        try:
            print(file)
            mistakes = main(r'{}'.format(str(file.get())))
            Label(root, text="* " + str(mistakes), font=("time new roman",10), fg='green').place(x=80,y=130)
        except FileNotFoundError:  Label(root, text="* Please use an existing file.", font=("time new roman",10), fg='red').place(x=20,y=20)
        except OSError:  Label(root, text="* No quotation marks in the file location.", font=("time new roman",10), fg='red').place(x=20,y=80)
    
    file.place(x=155,y=50)
     
    Button(root, text='Quit', width = 5,command=root.destroy).place(x=20,y=130)
    Button(root, text='Submit',width=5, command=fix_grammar).place(x=230,y=130)

    mainloop()

get_image()
