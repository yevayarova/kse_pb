#task1
chyslo = int(input("Введіть будь-яке число:"))
if chyslo % 2 == 0:
  print("Парне")

#task2
bal = float(input("Який у тебе GPA?)"))
if bal >= 90:
  print("Відмінник, красава")
elif bal >= 75:
  print("Молодець, теж нічо так")
else:
  print("Старайся більше, раб системи")

#task3
cina = 0
for cina in range(10,101,5):
  print(f"Ціна без ПДВ: {cina} -> з ПДВ: {cina*1.2}")

#task4
a = float(input("Введи будь-яке число:"))
b = float(input("Введи будь-яке число:"))
c = float(input("Введи будь-яке число:"))

if a>b:
  if a>c:
    print(f"{a}")
  else:
    print(f"{c}")
elif b>c:
  print(f"{b}")
else: 
  print(f"{c}")

if a>b and a>c:
  print(f"{a}")
if b>c and b>a:
  print(f"{b}")
if c>b and c>a:
  print(f"{c}")

#task5
groshi=1000
month=0
print(f"Станом на місяць номер {month}, ви накопичете {groshi}")
while groshi<=5000:
  groshi+=300
  month+=1
  print(f"Станом на місяць номер {month}, ви накопичете {groshi}")

#task6
rik = int(input("Високосність або звичайність якого року ти хочеш визначити?"))
if rik%4 == 0 and rik%100>0 or rik%400 == 0:
  print("Високосний")
else:
  print("Звичайний")

#task7
i=0
for i in range(21):
  if i%4 == 0:
    continue
  print(i)

#task8
credit=10000
misac=0
print(f"Станом на місяць номер {misac}, ваш залишок боргу становить: {credit}")
while credit>=0:
  credit -=1200
  credit=credit*1.02
  misac+=1
  print(f"Станом на місяць номер {misac}, ваш залишок боргу становить: {credit}")
  if credit ==0:
    break
print("Погасили нарешті, слава Богу")

#bonus
total_dohid = 0 
while True:
  dohid=float(input("How much did you earn this month?"))
  if dohid==0:
    break
  elif dohid<0:
    print("You can't  have negative income>:(")
    continue
  total_dohid+=dohid
  print(f"Your total income is {total_dohid}")