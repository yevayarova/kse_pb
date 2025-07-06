#Коментарі по ходу роботи
#я ще над жодним завданням стільки не мучилась, але претензій 0, нас попереджали 

# знаю що є багато іструментів на кшталт Alpha Vantage xb pandas-datareader, я обирала по статті https://www.linkedin.com/pulse/13-essential-python-libraries-free-market-data-everyone-kevin-meneses-u71jf
# і там топ1 це yahoo finance +++  на занятті ми його розбирали так що на цей раз не винаходитиму велосипед

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Збір даних
apple = yf.Ticker("AAPL")
hist = apple.history(period="3y")

#дуже приємно що коли юзаєш .history(period="3y") то yfinance відразу видає історію цін у форматі DataFrame

#Підготовка даних
display(hist)
#бачу що є колонки не потрібно для нашого аналізу, а саме Volume	Dividends	Stock Splits, підчищу
hist = hist[['Open', 'High', 'Low', 'Close']]
hist = hist.dropna()

#мені важливо щоб індексами цього датафрейму був час, бо інакше я не зможу використовувати .rolling(), .shift()  і будувати візуалізацію де дати будуть віссю на графіку
#зазвичай у фінансових таблицях індекс власне і є timestamp і тут наче не ивняток
hist.index = pd.to_datetime(hist.index)

#Розробка моделі ((╥﹏╥))

#"Просту стратегію" згадану в тз я зрозуміла так: 
#у нас є коротке ковзне середнє (я візьму 25 днів) і довге (50 днів), коротке швидше реагує на поточні зміни так як відображає сер знач коротшого періоду, довге змінюється повільшіне
#якщо коротке ковзне перетинає довге і стає вище за нього — це сигнал, що ціна почала рости швидше, ніж за довгий період, тобто тренд вгору, можна купувати. 
#Якщо коротка перетнула і пішла під довгу то вона відчула зміну на гірше швидше, отже для нас це сигнал продавати

#загалом логіка чудова, але щоб до неї дійти... тз:
# генеруєте сигнали купівлі або продажу на основі взаємодії! короткострокових і довгострокових ковзних середніх.
#оце "на основі взаємодії", от прям інтуїтивно очневидне.

# ще я нарешті зрозуміла чому нам таки потрібно ковзне середнє - воно згладжує шум, коливання що не репрезентують головний тренд ринку але відволікають.

# MA - moving average, далі юзатиму абревіатуру
# допомогло по MA в pandas https://stackoverflow.com/questions/40060842/moving-average-pandas
hist['MA25'] = hist['Close'].rolling(window=25).mean()
hist['MA50'] = hist['Close'].rolling(window=50).mean()
#беру для ковзного ціни закриття 
#і до речі я так поняла що перших 24 закриттів буде NaN  бо не буле з чого середнє за 25 порахувать

#Для сигналів вирішила надвати значення кожному закриттю, тобто додам колонку Signal де всі зщначення поки що будуть 0
hist['Signal'] = 0

#тут кожне закриття де мала ковзна вище за велику виставляю значення 1 = купляти 
hist.loc[hist['MA25'] > hist['MA50'], 'Signal'] = 1
#тут кожне закриття де мала ковзна нижче за велику виставляю значення -1 = продавати 
hist.loc[hist['MA25'] < hist['MA50'], 'Signal'] = -1


#За допомогою .diff() стоврю ще однк колонку з різницею станів і маючи -2 та 2 я можу бачити коли стан перейшов на купляти (=2) з -1 до 1,  і продавати (=-2) з 1 на -1 
hist['Trade'] = hist['Signal'].diff()
#ствовю окремі зрізи де треба куплятьі  продавать
buy_signals = hist[(hist['Trade'] == 2)].copy()
sell_signals = hist[(hist['Trade'] == -2)].copy()

#оце був гемор, поки поянал що можна викорисати .tolist() щоб перевести series в просто список 
#бо buy_signals та sell_signal можна додать в один список
# і на його довжину можна домножить buy та sell і коли вони посортуються по індексам (датам) то буде не просто  [buy, buy, buy, ..., buy] та [sell, sell, sell, ..., sell] а [buy, sell, buy, sell, buy, sell, buy, sell] 
signal_table = pd.DataFrame({
    "Date": pd.Series(buy_signals.index.tolist() + sell_signals.index.tolist()),
    "Price": pd.Series(buy_signals['Close'].tolist() + sell_signals['Close'].tolist()),
    "Action": ["Buy"] * len(buy_signals) + ["Sell"] * len(sell_signals)
}).sort_values("Date").reset_index(drop=True)


print("Таблиця сигналів:")
print(signal_table)

# 6. Розрахую прибуток/збиток  
profits = []
positions = []
actions = signal_table['Action'].tolist()
dates = signal_table['Date'].tolist()
prices = signal_table['Price'].tolist()

#щоб продати треба спочатку купити, тому беру "і" як купити тому кількість "і" буде len(actions)-1 бо останнє буде і+1 як продати
#можу рахувати прибуток використвючи for i in range бо транзакції посортавані за датами
for i in range(len(actions)-1):
    if actions[i] == "Buy" and actions[i+1] == "Sell":
        profit = prices[i+1] - prices[i]
        profits.append(profit)
        positions.append((dates[i], dates[i+1], prices[i], prices[i+1], profit))

total_profit = sum(profits)
#щось воно в кучу
print(" ")

print(f"Реалізований прибуток: ${total_profit:.2f} за 3 роки")

print(" ")

#для краси ще виведу кожну пару купівля продажу з їх датами
print("Транзакції:")
for pos in positions:
    print(f"{pos[0].date()} купівля по ${pos[2]:.2f} → {pos[1].date()} продаж по ${pos[3]:.2f} = {pos[4]:.2f}")
#ЗВИЧАЙНО я усвідослюю що можна було додати всі buy i sell і їх різницею був би profit, але ж треба зстраждати

#Додатково я зрозуміла наскільки важливий вибір власне часових рамок ковзних середніх, це може бути 30 і 100, 21 і 63 (як робочий місяць і квартал), 25 і 50. І від цього дуже (ДУЖЕ!!) пляше дохідність

#ніби візуалізаці в ТЗ не було, це більше особисте бажання цьому навчитись
plt.figure(figsize=(14, 7)) #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
plt.plot(hist.index, hist['Close'], label='Ціна закриття', linewidth=1) #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(hist.index, hist['MA25'], label='MA25', linewidth=1.5) 
plt.plot(hist.index, hist['MA50'], label='MA50', linewidth=1.5)
#Мені дууужуе кортілo приліпити якість маячки на точки де власне відбувається цей перетин + звичайно ці трикутнички будутьна самомму графіку закриттів не на ковзній
plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='g', label='Buy Signal', s=100, zorder=5) #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='r', label='Sell Signal', s=100, zorder=5)

#+ хочу позначити певні проміжки дат як також прийнятні для входу та виходу  зеленим та червоним (це не сигнали!)
plt.fill_between(hist.index, hist['Close'].min(), hist['Close'].max(), where=(hist['Signal']==1), color='green', alpha=0.10, label='Можна входити') #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html
plt.fill_between(hist.index, hist['Close'].min(), hist['Close'].max(), where=(hist['Signal']==-1), color='red', alpha=0.10, label='Варто виходити')


#нарешті
plt.title("AAPL")
plt.xlabel("Дата")
plt.ylabel("Ціна $")
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
