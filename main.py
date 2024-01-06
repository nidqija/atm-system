import atm_data







print("Welcome to Maybank!")

while True:
  passkey = str(input("Enter your passkey:"))



  for atm_data.method in atm_data.methods:
   print(atm_data.lines)
   print(atm_data.method)

  question = input("which one?")

  if question == "1":
      balance = float(input("Enter Balance:"))
      deposit = float(input("How much amount do you want to add?"))
      new_pay = balance + deposit
      print(f"Your new balance :RM{new_pay}")
   

  elif question == "2":
     amount = float(input("Enter Amount:"))
     withdraw = float(input("How much do you want to withdraw?:"))
     new_amount = amount - withdraw
     print(f"Your new amount is :RM{new_amount}")


  elif question == "3":

     for bill in atm_data.bills:
          print(atm_data.lines)
          print(bill)


          

     current_bill = str(input("Enter Bill type:"))

     if current_bill == '1':
          print(f'your tnb bill is RM{atm_data.tnb}')
          pay = float(input('Enter payment:'))
          deduc = atm_data.tnb - pay
          
          if pay < atm_data.tnb : 
               print(f'you have RM{deduc} left to pay ')
               rewind = str(input('do you want to pay more?(y/n)'))
               if rewind == 'n':
                     print(f'you current bill: RM{deduc}')
                     print('Thank you for using our service!')
               else:
                     pay = float(input('Enter payment:'))
                     deduc_plus1 = deduc - pay
                     print(f'you have RM{deduc_plus1} left to pay')
                     print('Thank you for using our service!')
                     

                    
                    
               
                    
                  

          else:
               print(f'you have RM{deduc} left to pay')
               print(f'Congratulations! You are fully-paid')
               print('Thank you for using our service!')
                    
                          
                                              
            





     elif current_bill == '2':
          print(f'your water bill is RM{atm_data.air}')
          pay = float(input('Enter payment:'))
          deduc_2 = atm_data.air - pay
          
          if pay < atm_data.air : 
               print(f'you have RM{deduc_2} left to pay ')
               rewind = str(input('do you want to pay more?(y/n)'))
               if rewind == 'n':
                  print(f'you current bill: RM{deduc_2}')
                  print('Thank you for using our service!')
               else:
                     pay = float(input('Enter payment:'))
                     deduc_2plus1 = deduc_2 - pay
                     print(f'you have RM{deduc_2plus1} left to pay')
                     print('Thank you for using our service!')
                     

                    
                    
               
                    
                  

          else:
               print(f'you have RM{deduc_2} left to pay')
               print(f'Congratulations! You are fully-paid')
               print('Thank you for using our service!')



     elif current_bill == '3':
          print(f'your tv broadcast bill is RM{atm_data.astro}')
          pay = float(input('Enter payment:'))
          deduc_3 = atm_data.astro - pay
          
          if pay < atm_data.astro : 
               print(f'you have RM{deduc_3} left to pay ')
               rewind = str(input('do you want to pay more?(y/n)'))
               if rewind == 'n':
                  print(f'you current bill: RM{deduc_3}')
                  print('Thank you for using our service!')
               else:
                     pay = float(input('Enter payment:'))
                     deduc_3plus1 = deduc_3 - pay
                     print(f'you have RM{deduc_3plus1} left to pay')
                     print('Thank you for using our service!')
               
          else:
               print(f'you have RM{deduc_3} left to pay')
               print(f'Congratulations! You are fully-paid')


     

     
  if input('Do you want to restart? (y/n):') ==  'n':
     print("Thank you for using our service!")
     break

                    









              




      

          
     
     


     
     

   







                    









              




      

          
     
     


     
     

   











              




      

          
     
     


     
     

   





