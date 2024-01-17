import openpyxl


wb = openpyxl.load_workbook("raziq.xlsx")
ws = wb['Sheet1']

title = print("Welcome to XYZ Bank!")
print("---------------------")





def login():
   while True:
      passkey = int(input("Please enter your passkey:"))
      if passkey == (ws['B2'].value):
        print(f"Welcome" , (ws['A2']).value )
        program()
        choice()
        break

      else:
         print("User not recognizable , please try again")
        
     



def choice():
  choice = float(input("Enter choice:"))
 
  if choice == 1 :
     print("Your current balance is RM" ,ws['C2'].value )
     amount = float(input("Enter amount: "))
     new_amount = ws['C2'].value + amount
     ws['C2'].value = new_amount
     print(f'Thank you! Your balance is now: RM {ws["C2"].value}')
     wb.save('raziq.xlsx')
    



  elif choice == 2:
     print("Your current balance is RM" , ws['C2'].value )
     withdraw = float(input("Enter cash widthdawal amount: "))
     new_balance =   ws['C2'].value - withdraw
     ws['C2'].value = new_balance
     print(f'Thank you! Your balance is now : RM {ws["C2"].value}')
     wb.save('raziq.xlsx')
     



  elif choice == 3:
      payment()


  elif choice == 'N':
     print("Thank you for using our service!")








def payment():
   print("Below are your bills:")
   print('------------------')
   print(ws['D1'].value ," = RM" , ws['D2'].value)
   print('------------------')
   print(ws['E1'].value , " = RM" , ws['E2'].value)
   print('------------------')
   print(ws['F1'].value , " = RM " , ws['F2'].value )



def program():
   print("Choose your errands:")
   print('------------------------------')
   print('1. Cash Deposit')
   print('------------------------------')
   print('2.Cash Withdrawal')
   print('------------------------------')
   print('3.Bill Payment')
   print('------------------------------')
   print("Enter your choice or type N to cancel")


login()

