import pandas as pd
import matplotlib.pyplot as plt

# Sorry, but this is more comfortable
# How much show rows
limit_on_displaying_lines = 5

# loading data
data = pd.read_csv('sevsu_subscribers.csv', sep=";")

# save how it was before
qua = len(data.index)

# delete non-informative profiles
data.dropna(subset = ["is_closed", "country_title", "city_title", "schools_name"], inplace=True)

# showing data
print (data.head(1000))

# info about data
index = data.index

print ("\n------------------")
print (f"Всего строк: {str(len(index))}\n")

print (f"\nПодсчитать количество участников по каждой стране\nTop {limit_on_displaying_lines}:")
# sampling by country
country = data.pivot_table(index=['country_title'], aggfunc='size').sort_values(ascending=False).head(limit_on_displaying_lines)
print (country)

print (f"\nПодсчитать количество участников по каждому городу\nTop {limit_on_displaying_lines}:")
# sampling by city
city = data.pivot_table(index=['city_title'], aggfunc='size').sort_values(ascending=False).head(limit_on_displaying_lines)
print (city)

print (f"\nПодсчитать количество участников по каждой школе для Севастополя\nTop {limit_on_displaying_lines}:")
# select only rows with the Sevastopol city id
school = data.loc[data['city_id'] == 185]
# sampling by schools name
school = school.pivot_table(index=['schools_name'], aggfunc='size').sort_values(ascending=False).head(limit_on_displaying_lines)
print (school)

# show... ahhhh...
names = ['До', 'После']
values = [qua, len(index)]
plt.suptitle('Очистка от не информативных аккаунтов')
plt.bar(names, values)
plt.show()

names = country.index.values
values = country.values
plt.suptitle(f'Количество участников по каждой стране \nTop {limit_on_displaying_lines}')
plt.bar(names, values)
plt.show()

names = city.index.values
values = city.values
plt.suptitle(f'Количество участников по каждому городу \nTop {limit_on_displaying_lines}')
plt.bar(names, values)
plt.show()

names = school.index.values
values = school.values
plt.suptitle(f'Количество участников по каждой школе для Севастополя \nTop {limit_on_displaying_lines}')
plt.bar(names, values)
plt.show()
