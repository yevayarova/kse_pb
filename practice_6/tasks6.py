#task 1
import geometry
y=4
x=6
print(geometry.rectangle_area(y,x))

#task2
import converter
print(converter.usd_to_uah(1000,39.5))
print(converter.uah_to_usd(1000,39.5))

#task3
import taxes
print(taxes.calculate_vat(15000))
print(taxes.calculate_income_tax(15000))

#tasks4
#квадратний корінь з 121
#синус числа π/2
#округлення вниз і вгору числа 7.8
import math

print(math.sqrt(121))
print(math.sin(math.pi/2))
print(math.floor(7.8))
print(math.ceil(7.8))

#task5
import random
print(random.randint(1,6))

#task6
#import datetime


#user_birthday = input("Введіть дату народження (рррр-мм-дд): ")
#birthday_date = datetime.datetime.strptime(user_birthday, "%Y-%m-%d")
#today = datetime.date.today()

#days_lived = (today - birthday_date.date()).days
#print(f"Ви прожили вже {days_lived} днів!")

#bonus

import random


balans=10000
max_plays = 1000
balance_history = [balans]

for i in range(max_plays):
    if balans<100:
        break
    zagadka_player = random.randint(0,37)
    ryletka = random.randint(0,37)
    balans-=100
    if zagadka_player == ryletka:
        balans += (100*36)
    balance_history.append(balans)
print(balance_history)
   
import matplotlib.pyplot as plt

plt.plot(balance_history)
plt.show()
