import csv

lists = [
     {"first_name" :"raziq" , "passkey"  : 123 , "balance" : 200 , "tnb" : 120 , "air" : 110 , "astro" : 130} ,
     {"first_name" :"alif" , "passkey"  : 135 , "balance" : 240 , "tnb" : 100 , "air" : 20 , "astro" : 140} ,
     {"first_name" :"adam" , "passkey"  : 234 , "balance" : 220 , "tnb" : 90 , "air" : 40 , "astro" : 150} ,
]


with open ('data.csv' , mode='w') as csvfile:
    fieldnames = ['first_name' , 'passkey' , 'balance' , 'tnb' , 'air' , 'astro']
    writer = csv.DictWriter(csvfile , fieldnames= fieldnames)
    writer.writeheader()
    for row in lists:
        writer.writerow(row)
        







