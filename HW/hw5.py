import requests
import pandas as pd
from datetime import timedelta


"1. Отримати прогнози погоди:"


# API взяла звідси https://open-meteo.com/en/docs 
#На цьому сайті в url параметрами є географічні координати: широта та довгота, тому для Києва треба ввести latitude = 50.45 longitude = 30.52
# я звичайно можу координати відразу в url вставити, але я хочу зробити код більш інтерактивним, тому юзер може вводити координати для отримання погоди
latitude = float(input("Ведіть широту перевівши мінути у десятковий залишок. Київ 50°27′00″= 50.45"\
"При бажанні отримати погоду південої півкулі ставте - перед широтою.  "))
longitude = float(input("Ведіть довготу перевівши мінути у десятковий залишок. Київ 30°31′25″= 30.52"\
"При бажанні отримати погоду західної півкулі ставте - перед довготою.  "))

url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,windspeed_10m&timezone=Europe%2FKyiv")
# щодо 7 днів: By default, we provide forecasts for 7 days. https://open-meteo.com/en/docs#hourly_weather_variables:~:text=By%20default%2C%20we%20provide%20forecasts%20for%207%20days
response = requests.get(url)
data = response.json()


"2. Перетворення даних:"


#я не відразу зрозуміла чому у змінних в доркументації api з теператури наприклад є тільки temperature_2m, 
#чому не можна 10m? а виявилось що це не змінний параметр це міжнароднйи метеоролгічнйи стандарт = вимірюваннч температури 2 метри над землею.
df = pd.DataFrame({ 
    'datetime': pd.to_datetime(data['hourly']['time']),
    'temperature': data['hourly']['temperature_2m'],
    'windspeed': data['hourly']['windspeed_10m'] # а ось швидкість вітру можна і 80 і 120 і 180, але 10 теж стандарт
})


"3.Виконайте базовий дослідницький аналіз даних (EDA):"


# отут якраз створюю змінну з даними за перші 3 дні = 72 години з моменту запиту
cutoff = df['datetime'].min() + timedelta(days=3)
df_3days = df[df['datetime'] < cutoff]

#базовий дослідницький аналіз даних (EDA)
print("Мінімальна температура:", df_3days['temperature'].min())
print("Максимальна температура:", df_3days['temperature'].max())
print(f"Середня температура: {df_3days['temperature'].mean():.1f}")

mean_wind = df['windspeed'].mean()
above_avg_hours = df[df['windspeed'] > mean_wind]
print("Кількість годин з вітром вище середнього:", above_avg_hours.shape[0]) #.shape[0] показує перший показник розміру тобиці = кількість рядків, тут якраз те що треба кількісь годн з вітром вище середнього

print(df)
