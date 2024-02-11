import openpyxl
import atm_data
import tkinter as tk
import ttkbootstrap as ttk
from atm_data import methods

root = tk.Tk()
root.geometry('800x600')
root.title('ATM System')
root.configure(bg='blue')
button = tk.Button(root , text = 'Start' , font=('Helvetica' , 20) ,height=1 , width= 30 , bg='yellow' , command=lambda:home_page())
button.pack(padx = 10 , pady= 20)




def home_page():
    global label
    home_frame = tk.Frame(root)
    title = tk.Label(root , text='Welcome to XYZ Bank!' , font=('Helvetica' , 35 , 'bold' ,) , bg='blue' , fg='yellow' )
    title.pack(padx= 20 , pady= 30)
    label = tk.Entry(root , text = 'Enter Account Number:' , font=('Helvetica' , 25) , bg='white' )
    label.pack()
    button = tk.Button(root , text = 'Submit' , font=('Helvetica' , 20) ,height=1 , width= 30 , bg='yellow' , command=lambda:choice_page())
    button.pack(padx = 10 , pady= 20)
    home_frame.pack()


def choice_page():
    global wb
    global sheet
    global label
    wb = openpyxl.load_workbook('raziq.xlsx')
    sheet = wb.active
    account_number = int(label.get())
    choice_frame = tk.Frame(root)  
    for row in sheet.rows:
        if account_number == row[1].value:
            welcome_label = tk.Label(choice_frame , text = f'Welcome! {row[0].value}' , fg='black' , font=('Helvetica' , 30))
            welcome_label.pack(padx=20 ,pady=20 ,side='top')

    
    choice_frame.pack()
      


             

      
    

root.mainloop()

