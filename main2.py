import openpyxl
import atm_data


wb = openpyxl.load_workbook('raziq.xlsx')
sheet = wb.active



title =print("Welcome To XYZ Bank!")

print('------------------------')
print('------------------------')
print('------------------------')








      


Valid = True












while Valid:  
       
       passkey = int(input('Enter Passkey:'))

       for row in sheet.rows:
          if row[1].value == passkey:
                   print(f'Hello ' , row[0].value)
              
               



                   for method in atm_data.methods:
                          print(method)
                          print('-----------------------------')
   


                   choice = int(input("Enter Choice:"))
 
                   if choice == 1:
                        print(f'Your current balance is:' ,row[2].value)

                        while True:
                             deposit = float(input("Enter Your Deposit:"))

                             if deposit <= 2000:
                                 new_deposit = row[2].value + deposit
                                 row[2].value = new_deposit
                                 print(f'Thank You! , Your new balance is : RM' , row[2].value)
                                 wb.save('raziq.xlsx')
                                 break

                             if deposit > 2000:
                                 print('Transaction must not exceed RM 2000 , please refer to the nearest HQ to do so')
                                 continue


       
      


                   elif choice == 2:
                        deduc = True
                        while deduc:
                             print(f'Your current balance is:' ,row[2].value)
                             while True:
                                  deduction = float(input("Enter Your Withdrawal Amount:"))
      
                                  if deduction < row[2].value:
                                        new_balance = row[2].value - deduction
                                        row[2].value = new_balance
                                        print(f'Thank You! , Your new balance is : RM' , row[2].value)
                                        wb.save('raziq.xlsx')
                                        deduc = False
                                        break
     

                                  else :
                                        print("Withdraw cannot exceed the intended balance!")
                                        continue





                   elif choice == 3:
                          print('These are your current bill:')
                          print(f' 1. TNB bill : RM' , row[3].value)
                          print(f' 2. Water bill : RM' , row[4].value)
                          print(f' 3. Astro bill : RM' ,row[5].value)
                          while True :
                               
                             bill = str(input('Enter Bill Type to pay:'))

                       
                    

                             if bill == '1':
                                    print(f'TNB bill : RM' , row[3].value)
                                    amount = float(input('Enter Amount: RM'))
                                    new_amount = row[3].value - amount
                                    row[3].value = new_amount
                                    print(f"Thank You! , Your Current Bill is : RM" , row[3].value)
                                    wb.save('raziq.xlsx')

                                    if row[3].value == 0:
                                          print('Congratulations ! your bill is fully paid!')

                                    break


  

                             elif bill == '2':
                                    print(f'Water bill : RM' , row[4].value)
                                    amount = float(input('Enter Amount: RM'))
                                    new_amount2 = row[4].value - amount
                                    row[4].value = new_amount2
                                    print(f"Thank You! , Your Current Bill is : RM" , row[4].value)
                                    wb.save('raziq.xlsx')

                                    if row[4].value == 0:
                                         print('Congratulations ! your bill is fully paid!')


                                    break


                             elif bill == '3':
                                    print(f'Water bill : RM' , row[5].value)
                                    amount = float(input('Enter Amount: RM'))
                                    new_amount3 = row[5].value - amount
                                    row[5].value = new_amount3
                                    print(f"Thank You! , Your Current Bill is : RM" , row[5].value)
                                    wb.save('raziq.xlsx')

                                    if row[5].value == 0:
                                          print('Congratulations ! your bill is fully paid!')

                                    break


                             else: 
                                    print("Invalid choice , please try again")
                                    continue



                   elif choice == 4:
                             print(f'Registered Name:' , row[0].value)
                             print(f'Balance: RM' , row[2].value)
                             print('Bills :')
                             print('------------------')
                             print('------------------')
                             print(f'TNB BILL : RM' , row[3].value)
                             print(f'WATER BILL : RM' , row[4].value)
                             print(f'ASTRO BILL : RM' , row[5].value)

                   else:
                        print('Invalid Choice , Please Try Again')


                        

          again =str(input("Run again ? (y/n):"))
 

          if 'y' in again:
                 
                  Valid = True
 
          else:
                  print("Thank you for using our service , see you soon!")
                  Valid = False

       


       else:
           print('Invalid passkey , please try again')
              


      






 









 








           
              












                 



  

      


  
      
      

    



     
    
     
       

            



            
            
      



       
   
    
















 








           
              












                 



  

      


  
      
      

    



     
    
     
       

            



            
            
      



       
   
    
















 








           
              












                 



  

      


  
      
      

    



     
    
     
       

            



            
            
      



       
   
    











              

      


  
      
      

    



     
    
     
       

            



            
            
      



       
   
    












              

      


  
      
      

    



     
    
     
       

            



            
            
      



       
   
    










