#task1
price_per_unit = "Нирка"
name_of_item = "IPhone"
height = 1.75
weight = 92 
nothing = None
hochesh_zyty = True
groshi_na_rakhunky = 999999999
string_data = "Текст"
is_student = True
has_studack = False 

#task2
a = 10
b = 20 

temp = a #зміна місцями
a = b
b = temp



a, b = b, a # або "кортеж розпакування"

a, b = b, a #ше раз

print(f"{a} {b}")

#task3
x = 3
y = 9

a = 2*x + 3*y
b = x**2 + 2*x*y + y**2
c = (2/8) * x - (13/7)*y
d = y**(4*x +2*y)**0.5
e = x%y
g = (y//x)**2
f = x>y
h = x**2==y

print (f"{a}, {b}, {c}, {d}, {e}, {g}, {f}, {h}")

#task4
name_of_item = "Пітса на Хрищатіку"

price_of_item = 500

needed_variable = name_of_item + " коштує " + str(price_of_item) + " гривнів."

print(needed_variable)

#task5
x1 = 5
x2 = 4 
x3 = 3
x4 = 2

checker = (x1 > x3) or (x2 > x4) and not (x2 != x3) or (x1 == x4)

print(checker)

#task6
height = float(input("Введіть ваш зріст в метрах (не пишіть м): "))
weight = int(input("Введіть вашу вагу в кілограмах (не пишіть кг): "))
bmi = weight/height**2
print (f"При вазі {weight} кг і рості {height} метрів, Ваш BMI складає {bmi}")

#bonus
import math
r = 30
r2 = 36.3
 
area = math.pi *(r**2)
area2 = math.pi *(r2**2)

diff = (area2/area - 1 )*100

diff ="{:.2f}".format(diff)

bb = " Друга піца на " + str(diff) + "% більша за першу"

print(bb)