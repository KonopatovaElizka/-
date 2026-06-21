import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Генерация данных
rng = np.random.default_rng()
numbers = rng.integers(-10000, 10001, size=1000)

# Формирование Series
series = pd.Series(numbers)

# Очистка данных от цифрового мусора
series = series.dropna()
series = series[(series >= -10000) & (series <= 10000)]
series = series.astype(int)

# Предварительный вывод
print(series)
print("Первые 5 элементов:", series.head())
print("Последние 5 элементов:", series.tail())

# Расчет числовых характеристик
min_value = series.min()
repeat_count = series.duplicated().sum()
max_value = series.max()
sum_value = series.sum()
mean_value = sum_value / len(series)
std_value = math.sqrt(((series - mean_value) ** 2).sum() / len(series))

print("Минимум:", min_value)
print("Количество повторяющихся значений:", repeat_count)
print("Максимум:", max_value)
print("Сумма:", sum_value)
print("Стандартное отклонение:", std_value)

# Линейный график исходных данных
plt.figure(figsize=(12, 4))
plt.plot(series.values)
plt.title("Линейный график исходного набора данных")
plt.xlabel("Номер элемента")
plt.ylabel("Значение")
plt.grid(True)
plt.show()

# Гистограмма значений, округленных до сотен
rounded_series = series.apply(lambda x: round(x, -2))

plt.figure(figsize=(12, 4))
plt.hist(rounded_series, bins=range(-10000, 10100, 100), edgecolor="black")
plt.title("Гистограмма значений, округленных до сотен")
plt.xlabel("Значение")
plt.ylabel("Количество")
plt.grid(True)
plt.show()

# Формирование DataFrame
ascending_series = series.sort_values().reset_index(drop=True)
descending_series = series.sort_values(ascending=False).reset_index(drop=True)

df = pd.DataFrame({
    "Исходные значения": series.reset_index(drop=True),
    "По возрастанию": ascending_series,
    "По убыванию": descending_series
})

print(df.head())

# Визуализация отсортированных данных
plt.figure(figsize=(12, 4))
plt.plot(ascending_series.values, label="По возрастанию")
plt.plot(descending_series.values, label="По убыванию")
plt.title("Сравнение отсортированных значений")
plt.xlabel("Номер элемента")
plt.ylabel("Значение")
plt.legend()
plt.grid(True)
plt.show()

