#1
hello = "Hello, Python World!"
print(hello)

#2
a = int(input("Придумайте число "))
b = int(input("І ще одне "))
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
if b !=0:
    print(f"a/b=,{a/b:.2f}")
else:
    print("Ділення на нуль неможливе")

#3
line1="Git"
line2="Hub"
sum_line= line1 + line2
lenght = len(sum_line)
print(f"Lenght of the line {sum_line} is {lenght}")

#4
#для того щоб число було парним або непарним має належати до множини цілих чисел
num =float(input("Insert a number"))
if num%1!=0:
    print("Ні парне ні непарне")
elif num%2==0: 
    print("Парне")
else:
    print("Непарне")


#можна написати також настпуний код, але він видаватиме помику якщо юзер ввееде не ціле число
num1 = int(input("Insert a number"))
if num1%2==0: 
    print("Парне")
else:
    print("Непарне")

#5
for i in range(1,11):
    print(i)
#або списком щоб місце не займало
list_num = []
for s in range(1,11):
    list_num.append(s)
print(list_num)

#6
usin=float(input("Введіть число"))
if usin>0:
    print("Позитивний")
elif usin<0:
    print("Негативний")
else:
    print("Нуль")

#7
for k in range(2,11,2):
    print(k)

#8
n = int(input("Введи число і просумую всі цілі чила від 1 до нього"))
sum_of_num = 0
for r in range(1, n+1):
    sum_of_num+=r
print(sum_of_num)

#9
for f in range(10,0,-1):
    print(f)

#10
for g in range(1,11):
    if g==5:
        continue
    if g==7:
        break
    print(g)