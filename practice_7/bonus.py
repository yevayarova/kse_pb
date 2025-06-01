import matplotlib.pyplot as pltt
import random

capital = 10000

ciny_start = {'A': 100, 'B': 200, 'C': 300}
invest_chastka = {'A': 0.4, 'B': 0.3, 'C': 0.3}

kilkist_akcij = {
'A': (capital * invest_chastka['A']) / ciny_start['A'],
'B': (capital * invest_chastka['B']) / ciny_start['B'],
'C': (capital * invest_chastka['C']) / ciny_start['C']
}

ciny_A = [ciny_start['A']]
ciny_B = [ciny_start['B']]
ciny_C = [ciny_start['C']]
portfelik = []

for misac in range(24):
    zmina_A = random.uniform(-0.05, 0.07)
    zmina_B = random.uniform(-0.05, 0.07)
    zmina_C = random.uniform(-0.05, 0.07)

    novi_ciny_A = ciny_A[-1] * (1 + zmina_A)
    novi_ciny_B = ciny_B[-1] * (1 + zmina_B)
    novi_ciny_C = ciny_C[-1] * (1 + zmina_C)



    ciny_A.append(novi_ciny_A)
    ciny_B.append(novi_ciny_B)
    ciny_C.append(novi_ciny_C)
    
    value = kilkist_akcij['A'] * novi_ciny_A + kilkist_akcij['B'] * novi_ciny_B + kilkist_akcij['C'] * novi_ciny_C

    portfelik.append(value)

max_value = max(portfelik)
min_value = min(portfelik)
average_return = (portfelik[-1] - capital) / capital * 100

print(f"Макс варість портфеля: {max_value:.2f} грн")
print(f"Мін вартістьи портфеля: {min_value:.2f} грн")
print(f"Сер дох за період: {average_return:.2f}%")

print(portfelik)
pltt.plot(portfelik)
pltt.title("Динаміка цінності портфеля")
pltt.xlabel("Місяць")
pltt.ylabel("Вартість портфеля (грн)")
pltt.grid(True)
pltt.show()