import openpyxl
import atm_data

wb = openpyxl.load_workbook('raziq.xlsx')
sheet = wb.active



title = print("Welcome To XYZ Bank!")
print('------------------------')
print('------------------------')
print('------------------------')


Valid = True

while Valid:
         
 passkey = int(input('Enter Passkey:'))

 for row in sheet.rows:
        if row[1].value == passkey:
            print(f'Hello ' , row[0].value)
            Valid = False



            for method in atm_data.methods:
               print(method)
               print('-----------------------------')
   


            choice = int(input("Enter Choice:"))

            if choice == 1:
                 print(f'Your current balance is:' ,row[2].value)
                 deposit = float(input("Enter Your Deposit:"))
                 new_deposit = row[2].value + deposit
                 row[2].value = new_deposit
                 print(f'Thank You! , Your new balance is : RM' , row[2].value)
                 wb.save('raziq.xlsx')
       
      


            elif choice == 2:
                deduc = True
                while deduc:
                     print(f'Your current balance is:' ,row[2].value)
                     deduction = float(input("Enter Your Withdrawal Amount:"))
      
                     if deduction < row[2].value:
                          new_balance = row[2].value - deduction
                          row[2].value = new_balance
                          print(f'Thank You! , Your new balance is : RM' , row[2].value)
                          wb.save('raziq.xlsx')
                          deduc = False
     

                     else :
                          print("Withdraw cannot exceed the intended balance!")





            elif choice == 3:
                    print('These are your current bill:')
                    print(f'TNB bill : RM' , row[3].value)
                    print(f'Water bill : RM' , row[4].value)
                    print(f'Astro bill : RM' ,row[5].value)
                    bill = str(input('Enter Bill Type to pay:'))
                    

                    if bill == 'TNB':
                         print(f'TNB bill : RM' , row[3].value)
                         amount = float(input('Enter Amount: RM'))
                         new_amount = row[3].value - amount
                         row[3].value = new_amount
                         wb.save('raziq.xlsx')




              

      


  
      
      

    



     
    
     
       

            



            
            
      



       
   
    










