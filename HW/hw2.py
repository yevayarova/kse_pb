#початковий рівень
#task 1.1

list1 = [1, 4, 67, 0.87, 500]
total1 = sum(list1)
print("List:", list1)
print("Sum of numbers is list equals to:", total1)

#але це занадто нудно 
"""
Я намагалася знайти як зробити МАКСИМАЛЬНО рандомний список з int i float 
І я вперлася в стелю  - як би я не намагалася рандомізувати показники, мені завжди потрібно вказати межі. 
це було просто було відкриттям для мене, що, виявляється в програмуванні немає хаосу. 
Комп'ютер не знає, що таке *будь-що*. 
Для того, щоб це було максимально рандомно, максимально чітко треба все прописати. 
І реального рандому ніколи не буде...
шок
Ось, що я наварганіла під кінець. 
Це хоч щось плюс-мінус рандомне
"""
import random
def random_number():
    type = random.choice(['int','float'])
    lower = random.randint(-10**6,0)
    upper = random.randint(1,10**6)

    if type == 'int':
        return random.randint(lower, upper)
    else:
        return random.uniform(lower, upper)

random_list = []
length = int(input("Введіть довжину списку: "))
for i in range(length):
    random_list.append(random_number())

sum_list_numbers =  sum(random_list)
print("Ось +- рандомний список: ", random_list)
print("І сума чисел цього списку: ", sum_list_numbers)

#ок тепер я задоволена

#task 1.2
list2 = [3, 598, 90.85, 108, 0.003, 10]
minimum =  min(list2)
print("Список: ", list2)
print("Найменше число зі списку це: ", minimum)

#task 1.3
list3= [4, 59, 857, 9999, 0.994, 2, 2.09, 12]
reversed_list3 = list3[::-1]
print("Список",list3)
print("Перевернутий список",reversed_list3)

#task 1.4
list4 = [3, 5, 8.9, 10, 8304, 30.098, 4994, 2]
even_list4 = []
for i in list4:
    if i%2 == 0:
        even_list4.append(i)
print("Список: ", list4)
print("Парні числа зі списку", even_list4)

#task 1.5
list5 = [2, 42, 8.893, 3, 10.8, 92, 698, 9.087]
print("Here is list: ", list5)
f = float(input("I will multiply each element in this list be a factor. Type a factor: "))
f_list5 = []
for i in list5:
   f_list5.append(i*f)
print (f"Done, each element of {list5} multiplied by {f}, resulting list is {f_list5}")

#середній рівень
#task 2.1
list6 = [3, 56, 709.75, 869.7, 89, 840, 2, 10, 0.0001]
print("List", list6)
x =float(input("Comparing number")) 
f_list6 = []
for i in list6:
    if i > x:
        f_list6.append(i)
print(f"Elements more than {x} are {f_list6}")

#task 2.2
list7 = [4, 45, 5905.5505, -48505, 2, -35, 1]
print("List", list6)
total = 0
count = 0
for i in list7:
    if i>0:
        total+=i
        count+=1
if total>0:
    print(f" Середнє значання додатних елементів списку: {(total/count):.2f}")
else:
    print("Список не має додатних чисел")
# округлила до двох знаків після коми просто щоб гарно було

#task 2.3 
list8 = [2345, 325, 5,  45.433, 43, 9, 2006, 3.094845, 1]
print(list8)
x  = float(input("Comparing number again ")) 
f_list8 = []
for i in list8:
    if i>x:
        f_list8.append(i)
if len(f_list8)>0:
    print(max(f_list8))
else:
    print("No numbers more than typed")

#task 2.4
list = [1, 3.3534, 85696, 8, 9475, -5758, 0, 2, 323, -1]
print("Наступні завдання будуть з списком:", list)
y = 2
sum_div = 0
for i in list:
    if i%y==0:
        sum_div+=i
print(f"Сума чисел, які діляться на {y} дорівнює: {sum_div}")

#task 2.5
q_list =[]
for i in list:
    q_list.append(i**2)
print("List with squared elements", q_list)

#task 2.6
p_list = []
for i in list:
    if i>0:
        p_list.append(i)
if len(p_list)> 0:
    print("List with positive elements", p_list)
else: 
    print("No elements in list were positive")

#task 2.7
words = ['apple', 'banana', 'application', 'apply', 'orange', 'app', 'goerge']
f_words = []
for i in words:
    if i.startswith('app'):
        f_words.append(i)
print(f_words)
#знайшла метод startswith() https://www.w3schools.com/python/ref_string_startswith.asp

#task 2.8
n = 3
n_sum = 0
for i in range(n, len(list)):
    n_sum += i
print("Сума перших", n, "чисел:", n_sum)

#task 2.9
words = ['madam', 'янесугусеня', 'око', 'абулуба', 'racecar', 'apple', 'noon']
palindromes = []
for i in words:
    if i == i[::-1]:
        palindromes.append(i)
print("Паліндроми:", palindromes)

#task 2.10
x = 2
divisibility = []
for i in list:
    if i % x == 0:
        divisibility.append(True)
    else:
        divisibility.append(False)
print("Подільність на", x, ":", divisibility)

#середній рівень 
#task 3.1
X = 5
Y = 10
f_list = []

for i in list:
    if i % X == 0 and i % Y != 0:
        f_list.append(i)

print("Діляться на", X, "але не на", Y, ":", f_list)

#task 3.2
list_with_lists = [[1,3,455,0.43,1], [2324], [3,34,2], [True, False], [None], ['yeeaa']]
just_list = []
for i in list_with_lists:
    for j in i:
        just_list.append(j)
print("Список зі списками ", list_with_lists)
print("Список просто з елементів розгорнутий ", just_list)

#task 3.3
text = "Вічний революціонер — дух, що тіло рве до бою, рве за поступ, щастя й волю — він живе, він ще не вмер. Ні попівськії тортури, ні тюремні царські мури, ані війська муштровані, ні гармати лаштовані, ні шпіонське ремесло в гріб його ще не звело. Він не вмер, він ще живе! Хоч від тисяч літ родився, то аж вчора розповився і о власній силі йде. І простується, міцніє, і спішить туди, де дніє: словом сильним, мов трубою, міліони зове з собою — міліони радо йдуть, бо се голос духа чуть. Голос духа чути скрізь: по курних хатах мужицьких, по верстатах ремісницьких, по місцях недолі й сліз. І де тільки він роздасться, щезнуть сльози, сум, нещастя, сила родиться й завзяття — не ридать, а добувати хоч синам, як не собі, кращу долю в боротьбі. Вічний революціонер — дух, наука, думка, воля — не уступить пітьмі поля, не дасть спутатись тепер. Розвалилась зла руїна, покотилася лавіна, і де в світі тая сила, щоб в бігу її спинила, щоб згасила, мов огонь, розвидняющийся день?"
uppercase_letters = []
for i in text:
    if i.isupper():
        uppercase_letters.append(i)
print("Великі літери у вигляді окремих підрядків:")
for i in uppercase_letters:
    print(i)       

#task 3.4
list_sort = [4, 66, 606, 77, 3, 8, 88, 8, -345.45, 1, 2.098, 1]
l_sorted1= sorted(list_sort, key=lambda x: (-x))
l_sorted2 = sorted(list_sort, key=lambda x: -list_sort.count(x))
print("Сортовані за спаданням:", l_sorted1)
print("Сортовані за частотою:", l_sorted2)
#обєднала
items_sorted = sorted(list_sort, key=lambda x: (-x, -list_sort.count(x)))
print(items_sorted)

#task 3.5
list8 
list6
combined = []
for i in list8:
    if i%2==0:
        combined.append(i)
for i in list6:
    if i%2==0:
        combined.append(i)
print("Об’єднаний список парних чисел: ",combined )
# я нарила як можна елементи списку скласти всписок без append і одночасно дві умовиї
combined = [i for i in list8 + list6 if i % 2 == 0]
print(combined)

#task 3.6
shop = [
    {"iphone": 5, "samsung": 3},
    {"xiomi": 2, "samsung": 4},
    {"samsung": 30, "iphone":49, "huawey": 60},
    {"iphone": 7, "xiomi": 1}
]
total = {}
for dict in shop:
    for phone in dict:
        if phone in total:
            total[phone] += dict[phone]
        else:
            total[phone] = dict[phone]
print("Сума продажів телефонів різних марок в магазині:")
print(total)

#task 3.7
print(list8)
changed_list = []
for i in list8:
    if isinstance(i, float) and not isinstance(i, int):
        changed_list.append("float")
    elif isinstance(i, float):
        changed_list.append("float (ціле флоат)")
    elif isinstance(i, int):
        changed_list.append("int")
    else:
        changed_list.append("не float і не int")
print(changed_list)
# я подумала що треба врахувати щзо 3.0 теж флоат, і ще ж модуть бути не числа +isinstance  навчилась

#task 3.8
print(words)
x=3
count = 0 
for i in words:
    if len(i)>X:
        count+=1
print("Кількість рядків довжиною більше", X, ":", count)

#task 3.9
list9 = ["water", "sand", "fire", "magic"]
list10 =["мокра", "сухий", "пекучий", "не існує"]
merged_list = []
min_length = min(len(list9), len(list10))
for i in range(min_length):
    merged_list.append(list9[i])  
    merged_list.append(list10[i])
print("Об’єднаний список по черзі:", merged_list)


#task 3.10
print(list)
X = 3
Y = 100
c_list = []
for i in list:
    if i > X:
        new_i = i * Y
        c_list.append(new_i)
    else:
        c_list.append(i)
print("Результат після множення за умовою:", c_list)


