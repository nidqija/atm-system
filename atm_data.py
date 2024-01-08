methods = ("1.Cash deposit" , "2.Cash Withdrawal" , "3.Pay" , )
lines = ("-------------")
bills = ("1.tnb" , "2.air" , "3.astro")

tnb = 150
air = 60
astro = 130

class customers:

    def __init__(self , name , passkey , balance , tnb , air , astro ):
         self.name = name
         self.passkey = passkey
         self.balance = balance
         self.tnb = tnb
         self.air = air
         self.astro = astro

custom_1 = customers('Raziq' , '123' , 500 , 120 , 140 , 100)
custom_2 = customers('Alif' , ' 246' , 300 , 100 ,40 ,40 )
custom_3 = customers('Adam' , '130' , 500 , 300 , 200 , 100)

print(custom_1)
        







