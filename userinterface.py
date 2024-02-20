import tkinter as tk

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)   

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        for F in (loginpage , welcomepage ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

           
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("loginpage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class loginpage(tk.Frame):
    
    def __init__(self, parent , controller):
        tk.Frame.__init__(self , parent)
        self.controller = controller
        self.configure(background='blue')
        title = tk.Label(self , text='Welcome to XYZ Bank!' , font=('Helvetica' , 35 , 'bold' ,) , bg='blue' , fg='yellow')
        title.pack(padx= 20 , pady= 30)
        label = tk.Entry(self , text = 'Enter Account Number:' , font=('Helvetica' , 25) , bg='white' )
        label.pack()
        button = tk.Button(self , text = 'Submit' , font=('Helvetica' , 20) ,height=1 , width= 30 , bg='yellow' ,command=lambda:controller.show_frame('welcomepage'))
        button.pack(padx = 10 , pady= 20)


class welcomepage(tk.Frame):
     def __init__(self, parent , controller):
        tk.Frame.__init__(self , parent)
        self.configure(background='blue')
        self.controller = controller
        title = tk.Label(self , text='Hello' , font=('Helvetica' , 35 , 'bold' ,) , bg='blue' , fg='yellow' )
        title.pack(padx= 20 , pady= 30)
     
    







if __name__ == "__main__":
    app = GUI()
    app.geometry('600x500')
    app.mainloop()
